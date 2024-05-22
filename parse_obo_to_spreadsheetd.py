#!/usr/bin/env python
# this script parses OBO files to give a csv with columns for each child ARO tag, 
# their functional description, followed by columns for higher level parents ARO tags
# and descriptions
# written by shawn whitefield 9-10-2015

from __future__ import division, print_function
import sys


infileName = sys.argv[1]
outfileName = sys.argv[2]

infile = open(infileName, 'r')
outfile = open(outfileName, 'w')

for line in infile:
	fields=line.strip().split()
	if line.startswith('id: ARO'):
		child = line.strip() # split()
		child=child.replace("id:","")
		child=child.split()
	if line.startswith('is_a:'):
		parent= line.strip()
		parent= parent.replace("is_a:",",")
		parent= parent.replace("!",",")
		child.append(str(parent)) # add the child to the row
		outLine=''.join(child) # make it tab delimited
		print(outLine, file=outfile)
	
	
outfile.close()
infile.close()	




# pseudocode below:
#for each [term] until empty line:
#read each line

#if it starts with id, put the rest of the line in a new row in column called ID
#if it starts with name put that in a column called name
#if it starts with namespace, put in a column called 
#if it starts with is_a: put the rest of the line until reach a ! in that row in column called parent
#		put anything after !
	#if there are multiple parents replicate all of the other stuff in the row on a new row
	#add another entry for parent column

