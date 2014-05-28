from Bio import SeqIO
from StringIO import StringIO
from Bio import AlignIO
import MySQLdb as mdb
import glob
import csv
import os

### get list of all genbank files
print "\n\nGetting a list of Genbank files..."
genbank_files = glob.glob("/home/lcoghill/Development/Genbank/*.gb") # get a list of all files in Genbank folder
file_count = len(genbank_files)
print "%s files successfully found.\n" %file_count
print "-"*50+"\n"

db = mdb.connect("localhost", "root", "reelab13", "phylota")
cursor = db.cursor()

### open each file
count = 0
csv_file = open('genbank.csv', 'w+')
w = csv.writer(csv_file, delimiter = ',')
for f in genbank_files:
    print "Processing Genbank file %s..." %f
    csv_data = []
    for record in SeqIO.parse(f, "genbank") :
        sql_query = "".join(['SELECT ti FROM taxid WHERE gi=',record.annotations['gi'],';'])
        cursor.execute(sql_query)
        ti = cursor.fetchone()
        csv_data.append(record.id) 
        csv_data.append(record.annotations['gi'])
        csv_data.append(record.annotations['organism'])
        if ti:
            csv_data.append(ti[0])
        else:
            csv_data.append("NA")
        csv_data.append(f[35:-3])
        csv_data.append(record.description.replace(',', ''))
        csv_data.append(str(record.seq).lower())
        w.writerow(csv_data)
        print "Record %s from file %s successfully written." %(record.annotations['gi'], f[35:-3])
        count += 1
    print "-"*100
    print "Conversion of file %s, complete." %f

csv_file.close()
print "%s records processed." %count


