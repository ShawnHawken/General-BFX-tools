#!/usr/bin/env python
'''
This script takes a file containing a column of file names and copies all of the files from 
a directory that have names that match the file-names in the file to a specified directory.
'''
from __future__ import division, print_function
import os
import shutil 
import re
import sys

FileNameList=sys.argv[1] #file containing file names of files to copy
OldDirectory=sys.argv[2] #directory and path to copy the files from
Match_NewDirectory=sys.argv[3] #directory and path to copy the files to


File_List = open(FileNameList, 'r') #open file containing file names
files= os.listdir(OldDirectory) #make a list of all the files in the directory
for file in files: #select the file to compare
	for row in File_List: #pick a name from the list #read the FileNameList file row by row
		fields = row.strip().split() #split the strings of file names
		for i in fields:
			for j in files: #if the name matches a file in the old directory
				if re.match(i, j):
					shutil.copy2((OldDirectory + "/" + j), Match_NewDirectory) # copy the file to the new directory 
 
#FileNameList.close()
