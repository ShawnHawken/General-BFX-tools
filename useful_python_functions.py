#!/usr/bin/env python
from __future__ import division, print_function
import re
IMPORT os
             
 
 # Ali's shared pythong 3
 
 /nfs/esnitkin/bin_group/anaconda3/bin/python
                   
                   
# FIND THE NUMBER OF TAGS AND DISTINCT TAGS IN AN XML FILE   
         
pat = re.compile((r'</([A-Za-z-_]+)')) 
                                                 
def get_tags(filename):   
	with open(filename) as file:
		closetags = pat.findall(file.read())
	print('the number of total tags was {}, of which {} were distinct' .format(len(closetags), len(set(closetags))))                                         
                                                                  
# TO PARSE AN XML FILE
import xml.etree.cElementTree as ETree   
tree = ETree.parse("./file")
root = tree.getroot() #get the root of a element tree
                  
                  
# find all of the names in the file          

#counts the tags in a element tree                                        
tags = set()
for element in tree.getiterator():
	tags.add(element.tag)
                                  
                                                  
# count how many times each tags occurs
counts = {}
for element in tree.getiterator():
	counts[element.tag] = 1 + counts.get(element.tag, 0)    
	
# find names of the tags in the tree

sortedtags = sorted(counts.items(),
					key = lambda item: item[1],
					reverse = True)

for item in sortedtags:
	print(item)                        

# get info associated with the tags

#blast hits

hits = root.getiterator('Hsp_positive')
hit1 = next(hits)
hit1.text
next(hits).text

# print elements of subtree tree

def print_element(element, level=1):
    if element.text and not element.text.isspace():
        print(' '*level, element.tag, ':', element.text.strip(), sep' ')
    elif element.attrib:
        print(' '*level, element.tag)
    for attr in sorted(element.keys()):
        print(' '*(level+2), attr, '=', element.get(attr))



# print subtree elements

def print_subtree(element, level =0):
	print_element(element, level)
	for subelt in element.getchildren():
		print_subtree(subelt, level+1)
		