#!/usr/bin/env python

from __future__ import division, print_function
import argparse
import os
import shutil 
import re
import sys
import glob
import subprocess

parser = argparse.ArgumentParser(description='''This program takes a directory of 
fasta formatted genome assemblies and the name of a .PBS file and creates a PBS file
for each one and submits the PBS to the cluster to run Prokka to annotate all of the 
genome assemblies in the directory in parallel.
created on December 9 2015
Author: Shawn Whitefield''')

parser.add_argument('-GD', help='Path to genome directory')
parser.add_argument('-PD', help = 'Path to directory to put PBS scripts and prokka results')
args=parser.parse_args()

assemblies = os.listdir(args.GD) #make a list of all the assemblies in current directory
GD=args.GD
PD=args.PD

pbs_name= ("assembly", "prokka.PBS")
# for assembly in assembly directory make a PBS script:
for assembly in assemblies:
	assembly_name= assembly.replace('.fasta','')#remove the .fasta from the assembly file name
	outdir= os.mkdir('/'.join([PD,assembly])) #make a directory for the assembly
	pbs_name= '_'.join([assembly_name, "prokka.PBS"]) #get the pbs unique file name
	pbs_file_path='/'.join([PD,assembly,pbs_name])
	output_dir='/'.join([PD,assembly])
	print(pbs_file_path)
	outfile= open(pbs_file_path , 'w+')#make a file in this directory for the PBS script #print PBS file stuff
	print("#!/bin/sh" , file = outfile)
	print("####  PBS preamble", file = outfile)
	outfile.write('\n')
	print(" ".join(["#PBS -N", assembly_name]), file = outfile)
	outfile.write('\n')
	print("# User info", file = outfile)
	print("#PBS -M swhitefi@umich.edu", file = outfile) #dont email yourself!
	outfile.write('\n')
	print("#PBS -m a", file = outfile) #only send a message for error. It sucks to get 28347 emails!
	outfile.write('\n')
	outfile.write('\n')
	print("# Change the number of cores (ppn=1), amount of memory, and walltime:", file = outfile)
	print("#PBS -l nodes=1:ppn=11,mem=46gb,walltime=01:00:00", file = outfile)
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
	#load modules 
	print("# module load med perl-modules prokka", file = outfile)
	print("# prokka -setupdb", file=outfile)
	#print prokka commands
	force="-force"
	print(" ".join(["prokka", "-kingdom Bacteria", "-outdir",]), output_dir ,force, " ".join(["-prefix", assembly_name]), "/".join([GD,assembly]), file= outfile)

        outfile.close() 

	#submit the PBS script
	os.chdir(output_dir)
	submit_job=' '.join(['qsub', pbs_file_path])
	subprocess.call(str(submit_job), shell=True) 




