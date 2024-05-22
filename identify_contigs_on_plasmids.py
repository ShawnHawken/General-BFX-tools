#!/usr/bin/env python
#import biopython modules for blasting and parsing blast output

from __future__ import print_function
import argparse
import os
from datetime import date
import re
from Bio import SeqIO
#from Bio import SearchIO
from Bio.Blast.Applications import NcbiblastnCommandline
from pprint import pprint as pp
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from collections import defaultdict
from prettytable import PrettyTable
import csv
import sys

#SETUP THE DATE FOR NAMING FILES

parser = argparse.ArgumentParser(description='''
The point of this script is to figure out which contigs came from a plasmid.

This script takes a blast database and a fasta formatted query and queries the blast database
and then identifies the hits and creates a fasta file containing these hits and then
blasts the hits as the query against a plasmid blast database and outputs blast output file
to identify if the contigs with came from a plasmid.
By Shawn Whitefield 1-25-2015

 ''')

parser.add_argument('-BDB', help='contig blast database')
parser.add_argument('-q', help = 'query fasta file')
parser.add_argument('-pBDB', help = 'plasmid blast database')
args=parser.parse_args()


#OPEN ALL OF THE NECESSARY FILES AND ASSIGN CL ARGUMENTS AS VARIABLES 
BDB=args.BDB	# contig blast database variable
q=args.q		# query fasta file variable
pBDB=args.pBDB	# plasmid  blast database variable


# DO THE BLASTING with blast n
blastn_cline = NcbiblastnCommandline(query=q, db=BDB, outfmt=5, out="{}_contig_blast_results.xml".format(date.today()))
stdout, stderr = blastn_cline()


# PARSE BLAST OUTPUT TO IDENTIFY THE HITS
result_handle = open("{}_contig_blast_results.xml".format(date.today()))
blast_records = NCBIXML.parse(result_handle) #iterator for multiple objects
for blast_record in blast_records:
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			alignment_title = str(alignment.title)
			contig_match = alignment_title.strip('No definition line') #these are the names of the contigs that contain the hit
			contig_hits_list = open('{}_contig_match_header_list.txt'.format(date.today()), 'a+')
			contig_hits_list.write(contig_match) # print the list to a file in the current directory
			contig_hits_list.write('\n')
contig_hits_list.close()

#FIGURE OUT HOW MANY HITS THERE ARE IN THE HEADER LIST IN ORDER TO STEP THROUGH THE BLAST
#RESULTS GENERATOR IN THE PLASMID DATABASE BLAST
n_header_matches = sum(1 for line in open('{}_contig_match_header_list.txt'.format(date.today())))
matches=list(range(0,n_header_matches))


# PULL OUT THE CONTIG SEQUENCES THAT MATCH THE HITS FROM THE ORIGINAL BLAST DATABASE
# MAKE THESE INTO A FASTA FILE

contig_blast_database=SeqIO.parse(BDB,"fasta") #get a handle for the blast database
seq_dict={} #make an empty dict

for record in contig_blast_database:
        seq_dict[record.id]=record.seq #make dictionary of ids from the BDB

for line in open('{}_contig_match_header_list.txt'.format(date.today()),'r'): #read header list and find the hits in the contigs matching and put them into a fasta file
        line=line.strip()
        if line in seq_dict.keys():
                hit_blast_database_contig = ">" + line + "\n" + seq_dict[line]
                contig_hits_file = open('{}_hit_blast_database_contigs.fasta'.format(date.today()), 'a+')
                print(hit_blast_database_contig, file=contig_hits_file)
                contig_hits_file.write('\n')
contig_hits_file.close()

# BLAST THE FASTA FILE WITH THE HITS AGAINST THE PLASMID BLAST DATABASE
# TO IDENTIFY THE PLASMID HITS

blastn_p_cline = NcbiblastnCommandline(query='{}_hit_blast_database_contigs.fasta'.format(date.today()), db=pBDB, outfmt=5, out='{}_plasmid_hits.xml'.format(date.today()))
stdout, stderr = blastn_p_cline()

# PARSE THE PLASMID HITS BLAST OUTPUT
final_plasmid_matches_file = open("{}_final_plasmid_matches.out".format(date.today()), 'a+') #open file to append plasmid blast results but only after filtering below

result_p_handle = open('{}_plasmid_hits.xml'.format(date.today())) #get handle for plasmid blast results
blast_p_records = NCBIXML.parse(result_p_handle) #get generator of blast results handle

# STEP THROUGH GENERATOR TO PULL OUT USEFUL INFO FROM PLASMID BLAST
# ONLY KEEP THE RECORDS WHERE THE ALIGNMENT LENGTH COVERS >= 50% OF THE QUERY LENGTH
# AND WHERE HSP IDENTITIES ARE >= TO 30% OF THE ALIGNMENT LENGTH
entry_list = {}
query_dict = defaultdict(dict) #the outermost dictionary

for match in matches: #read header list for number of times to go through generator 
	blast_p_record = next(blast_p_records) #a generator can only step through 1 time
	length_of_query = blast_p_record.query_letters #length of the query sequence
	for alignment in blast_p_record.alignments:	
		for hsp in alignment.hsps:
			if (hsp.align_length)/(length_of_query)*100 >= 50:  #filter for hsp alignment length coverage of query %
			#make a dictionary of queries containing a dictionary where the plasmids are the keys and the percentage hsp.align length/query is the value
				query_dict[blast_p_record.query][alignment.title] = (hsp.align_length)/(length_of_query)*100
				
				
#format the dictionary

genres = ['genome', 'plasmid', 'percent_coverage']

list_of_lists = []
for plasmid, percent in sorted(query_dict.items()):
    titles = []
    for genre in genres:
        try:
            titles.append(percent[genre])
        except KeyError:
            titles.append(0)
    list_of_lists.append(titles)

books_array = numpy.array(list_of_lists)
        
        
        
        
				
				print('length of subject', len(hsp.sbjct), file= final_plasmid_matches_file)
				print('hsp length', hsp.align_length, file= final_plasmid_matches_file)
				print('filter hsp.align length / length query', (hsp.align_length)/(length_of_query)*100, file= final_plasmid_matches_file)
				print('Query title', blast_p_record.query, file= final_plasmid_matches_file)
				print('align title', alignment.title,file= final_plasmid_matches_file)






			




