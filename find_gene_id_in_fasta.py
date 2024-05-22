#!/usr/bin/env python

from Bio import SeqIO
import sys

fasta_file=sys.argv[1]
id_file=sys.argv[2]
outfile=sys.argv[3]

#parse input id file
wanted = set(line.rstrip("\n") for line in open(id_file))

#make generator object of each record in the fasta file if the id is in wanted
records = (r for r in SeqIO.parse(fasta_file, "fasta") if r.id in wanted)

# print the output to a file
count = SeqIO.write(records, outfile, "fasta")

#print how many records matched or an error if some are missing
print "Saved %i records from %s to %s" % (count, fasta_file, outfile)
if count < len(wanted):
    print "Warning %i IDs not found in %s" % (len(wanted)-count, fasta_file)


