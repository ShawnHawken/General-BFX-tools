#!/usr/bin/env python

from __future__ import print_function
import argparse
import os
import re
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
import sys

###obsolete stuff!
parser = argparse.ArgumentParser(description='''This program parses blast output in XML format''')
	
parser.add_argument('-blastoutput', help='Blast output file in XML format')
parser.add_argument('-o', '--outfile', help='''Name of parsed outputfile''')
args=parser.parse_args()

result_handle = open(sys.argv1)

#### stuff that works:
from Bio.Blast.Applications import NcbiblastnCommandline

#make variable for blasting
blastn_cline = NcbiblastnCommandline(query="/nfs/esnitkin/Shawn/UM_CRE-1/UM-CRE_fasta/genome_fasta/genomes/UM-CRE-1-1_S2_L001_R1_l500_contigs.fasta", db="AR-genes-2.fa", evalue=0.001,outfmt=5, out="UM_CRE_1-1_blast_output.xml")

# do the blasting and create blast output file in XML format 
stdout, stderr = blastn_cline()

#open the blast file for reading

result_handle = open("UM_CRE_1-1_blast_output.xml")

# parse the file 

blast_records = NCBIXML.parse(result_handle)

#
blast_record = next(blast_records)

#

E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
             print('****Alignment****')
             print('sequence:', alignment.title)
             print('length:', alignment.length)
             print('e value:', hsp.expect)
             print(hsp.query[0:75] + '...')
             print(hsp.match[0:75] + '...')
             print(hsp.sbjct[0:75] + '...')

	
#### find record for given gene id list

from Bio import SeqIO

wanted = set(line.rstrip("\n") for line in open("variable_gene_list.txt"))

records = (r for r in SeqIO.parse("AR-genes-2.fasta", "fasta") if r.id in wanted)


count = SeqIO.write(records, "./test_output", "fasta")

print "Saved %i records from %s to %s" % (count, "./AR-genes-2.fasta", "./test_output")
if count < len(wanted):
    print "Warning %i IDs not found in %s" % (len(wanted)-count, "./AR-genes-2.fasta")








seq_record in SeqIO.parse("AR-genes-2.fasta","fasta"):

