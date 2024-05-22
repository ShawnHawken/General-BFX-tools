#!/usr/bin/env python



parser = argparse.ArgumentParser(Usage:'''This program downloads the most up-to-date
.gbff.gz files for genomes from specified genus and species from the NCBI database.'''

# written by Shawn Whitefield 07-16-2015

import os
import re
import sys
import datetime
import urllib

parser.add_argument('-gs', help='genus and species of ogranism in format Genus_species')
parser.add_argument('-l', help='what you want the prefix on downloaded files to be')

# get the genus_species and label variables

genus_species=args.gs
species_label=args.l

# download appropriate assembly summary.txt file from NCBI

urllib.urlretrieve("ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/{0}".format(genus_species) , filename="assembly_summary.txt")


 
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/$1/assembly_summary.txt


# setup genbank extension variable
genbank_ext='_assembly_summary.txt'

#setup assembly summary date label

datelist=[]
datelist.append(datetime.date.today())
assembly_name= ' '.join([str(datelist[0]),genbank_ext])