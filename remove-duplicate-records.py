from Bio import SeqIO
import glob
import re


## simple script to remove duplicate records (based on record.id) from a biopython SeqRecord object.

fasta_dir = ''
out_dir = ''

fasta_files = glob.glob(fasta_dir + "*.fas")

for f in fasta_files:
    search_str = fasta_dir + "(.+?).fas"
    file_name = re.search(search_str, f).group(1)
    print "Removing duplicate records from %s..." %f
    handle = open(f, 'r')
    present_recs = []
    for record in SeqIO.parse(handle, 'fasta'):
        if record.id not in present_recs:
            present_recs.append(record.id)
        else:
            print "%s is already present. Discarding." %record.id
    good_recs = []
    out_handle = open(out_dir+file_name+".fas", 'w')
    for record in SeqIO.parse(handle, 'fasta'):
        if record.id in present_recs:
            good_recs.append(record)

    
    SeqIO.write(good_recs, out_handle, 'fasta')
    out_handle.close()
