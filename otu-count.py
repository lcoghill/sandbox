import requests
import simplejson as json
import os
import fnmatch
import re

def get_remote_study(study):
    response = requests.get(url)
    

def get_local_studies():
    local_studies = []
    for root, dirnames, filenames in os.walk('phylesystem-1/study'):
      for filename in fnmatch.filter(filenames, '*.json'):
            local_studies.append(os.path.join(filename))


    return local_studies

def id_missing_studies(remote_studies, local_studies):
    missing_studies = []
    for s in remote_studies:
        if s.replace(".json", "") not in local_studies:
            missing_studies.append(s)
    return missing_studies


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

#response = requests.get('http://api.opentreeoflife.org/phylesystem/v1/study_list')
#remote_studies = json.loads(response.text)
#local_studies = get_local_studies()
#missing_studies = id_missing_studies(remote_studies, local_studies)

response = requests.get('http://api.opentreeoflife.org/phylesystem/v1/study/pg_100.json')
json_data = json.loads(response.text, object_hook=_decode_dict)

otus = []
for otu in json_data['data']['nexml']['otus']['otu']:
     otus.append(otu['@id'])

print len(otus)
