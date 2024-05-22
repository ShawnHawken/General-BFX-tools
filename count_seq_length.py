#This script counts the length of a fasta formatted sequence

import sys
from Bio import SeqIO
handle = open(sys.argv[1], 'rU')
lengths = map(lambda seq: len(seq.seq), SeqIO.parse(handle, 'fasta'))
print sum(lengths)/float(len(lengths))
count_fasta.py (END) 