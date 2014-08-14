from Bio import SeqIO
import MySQLdb
import glob
import re


def fetch_gi(acc, conn, cur):

    cur.execute("SELECT gi FROM acc_to_gi")
    row = cur.fetchone()
    if row is not None:
        gi = row[0]
    else:
        gi = '00000'

    return str(gi)

def fetch_taxid(gi, conn, cur):

    cur.execute("SELECT taxid FROM gi_to_taxid WHERE gi=%s" %gi)
    row = cur.fetchone()
    
    if row is not None:
        taxid = row[0]
    
    else:
        cur.execute("SELECT taxid FROM genes WHERE gi=%s" %gi)
        row = cur.fetchone()
        if row is not None:
            taxid = row[0]
        else:
            taxid = "00000"
        

    return str(taxid)

def convert_date(date):

    date_vars = date.split("-")
    monthDict={'JAN':'01', 'FEB':'02', 'MAR':'03', 'APR':'04', 'MAY':'05', 'JUN':'06', 'JUL':'07', 'AUG':'08', 'SEP':'09', 'OCT':'10', 'NOV':'11', 'DEC':'12'}
    if date_vars[1] in monthDict:
        num_month=monthDict[date_vars[1]]

    new_date = date_vars[0] + "-" + num_month + "-" + date_vars[2]

    return new_date
    



conn = MySQLdb.connect(user="root", passwd="reelab14", db="genbank")
cur = conn.cursor()
genbank_dir = '/home/lcoghill/Dev/genbank/flat/'
genbank_file_list = glob.glob(genbank_dir + '*.seq')
csv_f = open('genbank_eukrayotes.csv', 'a')


for gbfile in genbank_file_list:
    handle = open(gbfile, 'rU')
    print "Converting Genbank file %s..." %gbfile
    for record in SeqIO.parse(handle, "gb") :
        acc = record.id
        description = record.description.replace(",", "").strip(".")
        seq = record.seq
        gb_div = re.search('gb(.+?).seq', gbfile).group(1).upper()
    

        if record.features[0].qualifiers['organism']:
            organism =  record.features[0].qualifiers['organism'][0]
        elif record.annotations['organism']:
            organism = record.annotations['organism'][0]
        else:
            organism = 'ignotus'


        if record.features[0].qualifiers['mol_type']:
            mol_type = "".join(record.features[0].qualifiers['mol_type'])
        else:
            mol_type = 'ignotus'


        if record.annotations['taxonomy']:
            taxonomy = "|".join(record.annotations['taxonomy'])
        else:
            taxonomy = 'ignotus'


        if record.annotations['date']:
            date = convert_date(record.annotations['date'])
        else:
            date = '00-00-0000'


        if record.annotations['gi']:
            gi = record.annotations['gi']
        else:
            gi = fetch_gi(acc, conn, cur)

    
        #taxid = fetch_taxid(gi, conn, cur)
        line = ",".join([gi, mol_type, organism, taxonomy, date, gb_div, description, acc])
        csv_f.write(line+'\n')
    handle.close()

conn.close()
csv_f.close()
