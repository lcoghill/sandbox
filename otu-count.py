import requests
import simplejson as json
import csv
import time
import timeit

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def get_remote_otus(study):
    url = 'http://api.opentreeoflife.org/phylesystem/v1/study/%s.json' %study
    response = requests.get(url)
    json_data = json.loads(response.text, object_hook=_decode_dict)
    otus = []
    for otu in json_data['data']['nexml']['otus']['otu']:
        otus.append(otu['@id'])

    return otus

def save_otu_count(otu_count, study_count, run_time, total_otus, synth_study_count, unique_synth_otus, total_synth_otus):

    with open('otu-count.csv', 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter="\t", quotechar="'")
        csvwriter.writerow(['Date:'+time.strftime("%x")] + ['UniqueOTUS:'+otu_count] + ['TotalOTUS:'+total_otus] + ['TotalStudies:'+study_count] + ['UniqueSynthOTUS:'+unique_synth_otus] + ['TotalSynthOTUS:'+total_synth_otus] + ['SynthStudyCount:'+synth_study_count] + ['Runtime:'+run_time])


def parse_synth_study_ids(synthesis_list):
    synth_study_list = []
    for s in synthesis_list:
        if 'taxonomy' not in s:
            id = s.split("_")[1]
            if "ot" or "pg" not in id:
                id = "pg_" + str(id)
        synth_study_list.append(id)

    return synth_study_list



if __name__ == "__main__":
    
    start_time = timeit.default_timer()

    ''' Get list of studies in synthesis, and process for otus '''

    response = requests.post('http://api.opentreeoflife.org/treemachine/v1/getSynthesisSourceList')
    synthesis_list = json.loads(response.text, object_hook=_decode_dict)
    synth_study_list = parse_synth_study_ids(synthesis_list) 
    
    ''' Get all OTUS in all NeXSON files from phylesystem
        and calculate unique otus in synthesis and overall
    '''
    response = requests.get('http://api.opentreeoflife.org/phylesystem/v1/study_list')
    study_list = json.loads(response.text)
    #study_list = ['pg_1000', 'pg_100']  # short study list for testing purposes
    all_unique_otus = []
    total_otus = 0
    total_synth_otus = 0
    unique_synth_otus = []
    count = 1
    for s in study_list:
        #print "Getting OTUS for study %s, %s / %s..." %(s, count, len(study_list)) # tracker for testing purposes
        otus = get_remote_otus(s)
        for o in otus:
            if o not in all_unique_otus:
                all_unique_otus.append(o)
        total_otus = total_otus + len(otus)
        if s in synth_study_list:
            for o in otus:
                if o not in unique_synth_otus:
                    unique_synth_otus.append(o)
            total_synth_otus = total_synth_otus + len(otus)                
        count += 1
    

 
    ## process it all, and save it to to a csv file
    stop_time = timeit.default_timer()
    run_time = stop_time - start_time
    save_otu_count(str(len(all_unique_otus)), str(len(study_list)), str(run_time), str(total_otus), str(len(synth_study_list)), str(unique_synth_otus), str(total_synth_otus))
