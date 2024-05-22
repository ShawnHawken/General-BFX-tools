#!/usr/bin/env python
#import biopython modules for blasting and parsing blast output

from __future__ import print_function
import argparse
import os
from datetime import date
import re
from Bio import SeqIO
from Bio import SearchIO
from Bio.Blast.Applications import NcbiblastxCommandline
from pprint import pprint as pp
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import csv
import sys


parser = argparse.ArgumentParser(description='''
#this script introduces mutations into a DNA sequence and prints the amino acid changes that result.

# cl arguments:
	#for each segment (DNA sequence of interest):
	#list of nucleotide mutations to introduce -nuc_list
	#list of amino acid substitutions to verify -AA_list
	#fasta file with WT WSN33 for a given segment -wt_seq
	#amino acid sequence for that protein -aa_seq
	#name of DNA sequence
	
	example usage: 
	$ python2 verify_muts.py -mut_list PB1_mutation_list -aa_list PB1_aa_mut_list -wt_seq WT_PB1_copy.txt -aa_seq PB1_wsn33_fludb_protein.fasta -seg PB1

By Shawn Whitefield 7-05-2016

 ''')

parser.add_argument('-mut_list', help='list of nucleotide mutations to introduce')
parser.add_argument('-aa_list', help = 'list of amino acid substitutions to verify')
parser.add_argument('-wt_seq', help = 'fasta file with WT WSN33 for a given segment')
parser.add_argument('-aa_seq', help = 'blast database with amino acid sequence for that protein')
parser.add_argument('-seg', help = 'name of segment or protein for naming output files')
args=parser.parse_args()


#OPEN ALL OF THE NECESSARY FILES AND ASSIGN CL ARGUMENTS AS VARIABLES 
mut_list=args.mut_list	
wt_seq = args.wt_seq
aa_seq = args.aa_seq
aa_list = args.aa_list
seg = args.seg

#read in wt file and introduce all mutations from mut list
f = open(wt_seq,'r' )
PB2 = ''.join(f.readlines()[1:]).replace('\n','')
PB2 = list(PB2)

with open(mut_list, 'r') as mut_list:
	for mutation in mut_list:
		mutation = mutation[1:] #remove original nucleotide from list   
		print(mutation)
		pos= re.findall('\d+',mutation)
		pos = int(''.join(pos))
		nuc = " ".join(re.findall("[a-zA-Z]+", mutation))
		PB2[pos-1] = nuc # introduce the mutation, python counts from 0


PB2_all_mutants = ''.join(PB2) #convert from list to string
filename = str(seg)+ "_all_mutants.fasta"
outfile = open(filename,"w") #open output file

f = open(wt_seq,'r' ) #open wt seq to get header line
header = ''.join(f.readlines()[0]).replace('\n','')
print(header, file = outfile) #print header to file
print(PB2_all_mutants, file = outfile) #print mutated sequence to file
outfile.close() #close output file


# PERFORM BLASTX MUTATED NUC QUERY VS WT PROTEIN SUBJECT
# DO THE BLASTING with blast x
blast_out = str(seg) + "_blast.out"

blastx_cline = NcbiblastxCommandline(cmd='blastx',query=filename, subject=aa_seq, outfmt="\'6 qseqid sseqid qstart qend qseq btop\'", out=blast_out)
stdout, stderr = blastx_cline()


#READ IN BLAST OUTPUT SPLIT ON TABS TO GET ONLY MUTANT AMINO ACID SEQUENCE
with open(blast_out,'r') as f:
    mut_prot = zip(*[line.split() for line in f])[4]
	
mut_prot = list(str(mut_prot).split(",")[0].replace('(',""))[1:] #convert mut_prot to a list for indexing
print(mut_prot)
mut_prot = mut_prot[0:len(mut_prot)-1] #remove extra ' character at the end
print(mut_prot)
#search for all of the AA substitutions from the list
# print the original position substitution


with open(aa_list, 'r') as AA_list:
	for sub in AA_list:
		print("mutation to verify", sub)
		sub = sub[1:] #remove original nucleotide from list   
		pos= re.findall('\d+',sub) #get the numeric position
		pos = int(''.join(pos))
		AA = " ".join(re.findall("[a-zA-Z]+", sub))
		print("supposed to be", AA)
		actual_change = mut_prot[pos-1]
		print("actual change", actual_change)
		print('\n')
		
