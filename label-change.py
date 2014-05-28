import glob
from Bio import AlignIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
__author__ = 'lcoghill'

alignment_files = glob.glob('alignments/*.alignment.fasta')
fasta_files = glob.glob('expanded-fasta/*.fasta')

count = 1
for f in alignment_files:
    new_alignment = []
    print "Correcting file %s / %s..." % (count, len(alignment_files))
    clean_name = f.split("/")
    clean_name = clean_name[1].replace(".alignment.fasta", "")
    fasta_file = "expanded-fasta/"+clean_name+".fasta"
    alignment = AlignIO.read(open(f), "fasta")
    seq_list = SeqIO.parse(open(fasta_file), "fasta")
    seq_names = []
    for s in seq_list:
        seq_names.append(s.name)
    for a in alignment:
        for s in seq_names:
            if a.id.replace("gi|", "") in s:
                a.id = a.id.replace(a.id, s)
                dummy = SeqRecord(Seq(str(a.seq)), id=a.id)
                new_alignment.append(dummy)

    out_file = "new-alignments/"+clean_name+".alignment.fasta"
    output_handle = open(out_file, "w")
    SeqIO.write(new_alignment, output_handle, "fasta")
    output_handle.close()
    count += 1
