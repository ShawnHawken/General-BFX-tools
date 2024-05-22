#!/usr/bin/env python

from __future__ import division, print_function
from pandas import *
import pandas as pd
import numpy as np
import sys
import collections
import re 

# make a dictionary out of every line where the antibiotic/first word on each line is the key
#and the other 

words = collections.defaultdict(list)
with open('/Users/shawnwhitefield/Desktop/Snitkin_lab/UM_CRE-1/UM_CRE_antibiogram/2015-12-15_VITEK_export/single_organisms/091403083') as f:
	lines = [l.strip() for l in f if l.strip()]	
	lines=str(lines).replace('\\t',' ') #delete the tabs
	line_list = lines.split(",")#convert string to list based on , sep these are the keys
	first_in_line=str(line_list).split(" ") #list for each line
	first_in_line_list=str(first_in_line).split(',')
		
	
	
	#make the dictionary keys
for line in first_in_line:
	words[line.split('')[0]].append(line)
	

	re.split('\t ',str(line))[0] #get the first word of the list
	
	
	
	words[line[0].append(line)
	
	
	
	
	words[word[0]].append(word)



		word.split(":")[0]#split line on white space
