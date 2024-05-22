#!/usr/bin/env python

from __future__ import print_function
import argparse
import os
import re
import sys

parser = argparse.ArgumentParser(description='''This program takes a directory of genomes
and the name of a .PBS file and creates a PBS file to run Mugsy to perform multiple genome
alignment on all of the .fasta genome files in the directory.  After you run this script
you will need to specify the path to mugsy in the output file
and you will want to change the name of your flux run in the PBS preamble''')
	
parser.add_argument('-GD', help='Path to genome directory')
parser.add_argument('-mOD', help = 'Path to mugsy output directory')
parser.add_argument('-p', help = 'prefix to name .MAF mugsy output file')

parser.add_argument('-o', '--outfile', help='''Name of .PBS file to make.''')
args=parser.parse_args()

#get genome files from the directory specified in -GD
genome_files = os.listdir(args.GD)
outfile = open(args.outfile, 'w')
GD=args.GD

#print PBS file stuff
print("#!/bin/sh", file = outfile)
print("####  PBS preamble", file = outfile)
outfile.write('\n')
print("#PBS -N WHAT_TO_CALL_FLUX_JOB", file = outfile)
outfile.write('\n')
print("# User info", file = outfile)
print("#PBS -M swhitefi@umich.edu", file = outfile)
outfile.write('\n')
print("#PBS -m abe", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("# Change the number of cores (ppn=1), amount of memory, and walltime:", file = outfile)
print("#PBS -l nodes=1:ppn=11,mem=46gb,walltime=48:0:00", file = outfile)
print("#PBS -j oe", file = outfile)
print("#PBS -V", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("# Change \"example_flux\" to the name of your Flux allocation:", file = outfile)
print("#PBS -A esnitkin_fluxod", file = outfile)
print("#PBS -q fluxod", file = outfile)
print("#PBS -l qos=flux", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("####  End PBS preamble", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("#  Show list of CPUs you ran on, if you're running under PBS", file = outfile)
outfile.write('\n')
print("if [ -n \"$PBS_NODEFILE\" ]; then cat $PBS_NODEFILE; fi", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("#  Change to the directory you submitted from", file = outfile)
print( end = ' ')
print("if [ -n \"$PBS_O_WORKDIR\" ]; then cd $PBS_O_WORKDIR; fi", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("#  Put your job commands here:", file = outfile)
outfile.write('\n')
outfile.write('\n')
print("# Commands to run Mugsy muliple genome alignment", file = outfile)
outfile.write('\n')
outfile.write('\n')
outfile.write('\n')
#print commands to run Mugsy
#variable for directory to output data to
mugsyOutDir = args.mOD
prefix = args.p
#prefix to name .MAF file

mugsStuff = " ".join(["mugsy --directory", mugsyOutDir, "-p", prefix])
#print the genomes
for i in genome_files:
	print('/'.join([GD,i]), end=' ', file = outfile)





	






outfile.close()