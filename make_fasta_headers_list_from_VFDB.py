#!/usr/bin/env python

# This script takes a file of fasta headers, splits on white space and outputs a 
# tab delimited file with 1 row for each header


from __future__ import division, print_function
import sys


infileName = sys.argv[1]
outfileName = sys.argv[2]

for line in infile:
	fields=line.strip().split()
	if line.startswith('>'):
		entry = line.strip() # split()
		entry=entry.replace(">","")
		entry=entry.split()
		outLine=''.join(entry) # make it tab delimited
		print(outLine, file=outfile)



infile = open(infileName, 'r')
outfile = open(outfileName, 'w')

#remove the > from beginning of a line

#make the file tab delimited







outfile.close()
infile.close()