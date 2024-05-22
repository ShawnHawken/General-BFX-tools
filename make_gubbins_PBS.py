#!/usr/bin/env python
'''
This script takes a directory of directories containing alignment files and generates
a PBS script for Gubbins from each alignment in the directory. Then it submits the PBS
scripts to run gubbins on the flux. Must be run from parent directory of alignment
directoires
Usage: python make_gubbins_PBS.py 

created on July 21, 2015
Author: Shawn Whitefield
'''
from __future__ import division, print_function
import os
import shutil 
import re
import sys
import glob
import subprocess

assemblies = os.listdir(".") #make a list of all the assembly directories in current directory

for directory in assemblies:
	dir_path = "".join(['./',str(directory)]) #append the path of this directory
	os.chdir(dir_path) #change directory to assembly directory
	outfile = open(''.join([directory,'_gubbins.PBS']), 'w+')	#make a file in this directory for the PBS script
	outfile_name=str(''.join([directory,'_gubbins.PBS']))
	flux_name = str(directory) # what to call this job in PBS script
	tree = glob.glob('./*.tree') #save tree file path as list variable
	for i in tree:
		tree = i  #get rid of quotes
	fullmsa = glob.glob('./*.fullmsa') # save full msa path as list variable
	for j in fullmsa:
		fullmsa = j # get rid of quotes
	# print PBS stuff to the outfile
	print("#!/bin/sh", file = outfile)
	print("####  PBS preamble", file = outfile)
	outfile.write('\n')
	print("#PBS -N", flux_name, file = outfile)
	outfile.write('\n')
	print("# User info", file = outfile)
	print("#PBS -M swhitefi@umich.edu", file = outfile)
	outfile.write('\n')
	print("#PBS -m abe", file = outfile)
	outfile.write('\n')
	outfile.write('\n')
	print("# Change the number of cores (ppn=1), amount of memory, and walltime:", file = outfile)
	print("#PBS -l nodes=1:ppn=11,mem=46gb,walltime=24:00:00", file = outfile)
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
	print("# Commands to run Gubbins recombination filter", file = outfile)
	outfile.write('\n')
	outfile.write('\n')
	outfile.write('\n')

# print the gubbins stuff to the outfile.
	gubbins_stuff = " ".join(["run_gubbins.py", "".join(['.',fullmsa]), "-s", ''.join(['.',tree]), "-t fasttree"])
	print("# Gubbins requires module load med python biopython dendropy reportlab fasttree RAxML fastml/gub gubbins", file = outfile)
	
	print(gubbins_stuff, file = outfile)

# close the new PBS file
	outfile.close()
	
# make a gubbins directory in the alignment directory

 	os.mkdir("".join(["Gubbins_",str(directory)]))
 	gub_dir = "".join(["Gubbins_",str(directory)])	
# move the outfile to the gubbins directory
	current_path = str("/".join([os.getcwd(), outfile_name]))
	gub_dir_path = str("/".join([os.getcwd(),gub_dir,outfile_name]))
	submit_job_path = str("/".join([os.getcwd(),gub_dir]))
	shutil.move(current_path, gub_dir_path)

#submit the Gubbins job
	os.chdir(submit_job_path)
	submit_job = ' '.join(['qsub', gub_dir_path])
	subprocess.call(str(submit_job), shell=True)
	os.chdir("../../")







