from Bio import AlignIO
import glob
import re


output_dir = 'phylip-alignments/'
alignment_files = glob.glob('alignments/*.fasta')
output_format = 'phylip-relaxed'
input_format = 'fasta'

for f in alignment_files:
    align = AlignIO.read(f, "fasta")
    file_name = re.search('/(.+?).den', f).group(1)
    print "Converting file %s..." % file_name
    AlignIO.convert(f, input_format, output_dir+file_name+".phy", output_format, alphabet=None)





