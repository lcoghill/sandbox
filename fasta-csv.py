import os
from Bio import SeqIO




print "Please enter the name of your nucleotide file from Genbank."
file_name = raw_input("Filename: ")
print "Opening %s" % file_name

## Iterate through each record in the fasta file, parse out the important information and write that information to a csv file
f = open(file_name,'r+') # nt fasta file
csv_file = "".join([file_name,".csv"])
csv = open(csv_file, "w+") #output csv file

count = 0
for record in SeqIO.parse(full_file_name, "fasta") :
    seq_list = record.description.split("|")
    csv_string = '%s, %s, %s' % (seq_list[1], seq_list[3], record.seq) #convert record to string
    csv.write("%s\n" % csv_string)
    print "Record %s converted to CSV format" %count
    count = count + 1
f.close()
csv.close()
