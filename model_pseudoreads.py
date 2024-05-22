#!/usr/bin/env python

from __future__ import division, print_function
import argparse
import os
import shutil 
import re
import sys
import glob
import random
import pandas as pd
import numpy as np
import csv
from collections import defaultdict
from collections import Counter
import subprocess

parser = argparse.ArgumentParser(description='''this script:
takes as arguments:
	1. fasta file containing genome sequence with header line removed
	2. n, number of bases to test on each side of insertion site
	3. number of 50,000 size subsamples to take 
	4. output file name 
What this script does:	
1. finds all of the TA dinucleotides in the genome
2. extracts a random subset (50,000)
3. picks n bases on each side of the TA dinucleotide
4. maps the flanking bases + TA sequence (stand in for the insertion site + n 
bases up and down stream) for each dinucleotide back to the genome
5. generates a tab delimited file with the insertion+ flanking sequence, its location(s) and how many places it maps
6. then you can read this file into R and make a histogram to see what range of n is optimal (results in the most 1-hit insertion+ flanking sequences)
created on April 18 2016
Author: Shawn Whitefield''')


parser.add_argument('infile', help='Name of a DNA fasta file containing genome')
#parser.add_argument("flanking_bases", default=10, help='# of flanking bases to test')
#parser.add_argument("sampling", default=1, help='# of subsamples of size 50,000 to take from all AT sites in genome')
parser.add_argument('output_file', help='name offile to print insertion sites to')
args=parser.parse_args()

output_file=open(args.output_file,'a+')



with open(args.infile, 'r') as genome:
	seq=genome.read().replace('\n', '')
#locations=list([seq.start() for seq in re.finditer('(?=AT)', seq)]) # find all of the locations of AT including overlaps
	locations = [i for i in range(len(seq)) if seq.startswith('AT', i)]

insertion_list=[] #initialize list for insertion sequences
insertion_loc=[] #initialize list for insertion locations

for location in locations:
	insertion_list.append(seq[location-16:location+2]) #make list of insertion sequences
	
for i in insertion_list:
	print(i,",",file=output_file)#make list of insertion locations
	

	
		

	


