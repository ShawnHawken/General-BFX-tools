#!/usr/bin/env python

# this program parses antibiogram data from the UM clinical lab into a tab delim spreadsheet format.
# this is for antibiotics on the UM panel: GNARUM1F on the TREK system

#Written by Shawn Whitefield 9-29-2015
#modified 12-15-2015 to be able to parse VITEK system antibiogram data

from __future__ import division, print_function
from pandas import *
import pandas as pd
import numpy as np
import sys


infileName = sys.argv[1]
outfileName = sys.argv[2]

infile = open(infileName, 'r')
outfile = open(outfileName, 'w')

print("specimen","organism",
			"Amikacin_symbol", "Amikacin_MIC", "Amikacin_result",
			"Ampicillin_symbol","Ampicillin_MIC","Ampicillin_result",
			"Ampicillin_Sulbactam_symbol","Ampicillin_Sulbactam_MIC","Ampicillin_Sulbactam_result",
			"Aztreonam_symbol","Aztreonam_MIC","Aztreonam_result",
			"Cefazolin_symbol","Cefazolin_MIC","Cefazolin_result",
			"Cefepime_symbol","Cefepime_MIC","Cefepime_result",
			"Cefotaxime_symbol","Cefotaxime_MIC","Cefotaxime_result",
			"Cefotaxime_clavulanic_acid_symbol","Cefotaxime_clavulanic_acid_MIC","Cefotaxime_clavulanic_acid_result",
			"Ceftazidime_clavulanic_acid_symbol","Ceftazidime_clavulanic_acid_MIC","Ceftazidime_clavulanic_acid_result",
			"Cefuroxime_sodium_symbol","Cefuroxime_sodium_MIC","Cefuroxime_sodium_result",
			"Ciprofloxacin_symbol","Ciprofloxacin_MIC","Ciprofloxacin_result",
			"Colistin_symbol","Colistin_MIC","Colistin_result",
			"Ertapenem_symbol","Ertapenem_MIC","Ertapenem_result",
			"Fosfomycin_Glucose6Phosphate_symbol", "Fosfomycin_Glucose6Phosphate_MIC","Fosfomycin_Glucose6Phosphate_result",
			"Gentamicin_symbol", "Gentamicin_MIC","Gentamicin_result",
			"Levofloxacin_symbol", "Levofloxacin_MIC", "Levofloxacin_result", 
			"Meropenem_symbol", "Meropenem_MIC", "Meropenem_result", 
			"Nitrofurantoin_symbol","Nitrofurantoin_MIC","Nitrofurantoin_result",
			"Piperacillin_Tazobactam_symbol", "Piperacillin_Tazobactam_MIC","Piperacillin_Tazobactam_result",
			"Tigecycline_symbol","Tigecycline_MIC", "Tigecycline_result",
			"Tobramycin_symbol", "Tobramycin_MIC","Tobramycin_result",
			"Trimethoprim_Sulfamethoxazole_symbol", "Trimethoprim_Sulfamethoxazole_MIC","Trimethoprim_Sulfamethoxazole_result",
		
 sep='\t', file=outfile)

for line in infile:
	rowdata = []
	fields=line.strip().split(",") #list of lines
	for line in fields:
		if line.startswith('"Specimen"	":"'):
			ID=line.split("\t")[2] #ID
			
		if line.startswith('Alt Patient ID:'):
			ID=line.split("\t")[4] #mrn number
			
		if line.startswith("Source:"):
			source=line.split("\t")[2] #body site source
			
		if line.startswith('"Amikacin"'):
			Amikacin_symbol =line.split("\t")[1]
			Amikacin_MIC =line.split("\t")[2]
			Amikacin_result =line.split("\t")[3]
			#print(Amikacin) #Amikacin
		
		if line.startswith('"Ampicillin"'):
			Ampicillin_symbol =line.split("\t")[1]
			Ampicillin_MIC =line.split("\t")[2]
			Ampicillin_result =line.split("\t")[3]
			#print(Ampicillin) #"Ampicillin"
			
		if line.startswith('"Ampicillin/Sulbactam"'):
			Ampicillin_Sulbactam_symbol =line.split("\t")[1]
			Ampicillin_Sulbactam_MIC =line.split("\t")[2]
			Ampicillin_Sulbactam_result =line.split("\t")[3]
			#print(Ampicillin_Sulbactam) #Ampicillin_Sulbactam
			
		if line.startswith('"Aztreonam"'):
			Aztreonam_symbol =line.split("\t")[1]
			Aztreonam_MIC =line.split("\t")[2]
			Aztreonam_result =line.split("\t")[3]
			#print(Aztreonam) #Aztreonam
			
		if line.startswith('"Cefazolin"'):
			Cefazolin_symbol =line.split("\t")[1]
			Cefazolin_MIC =line.split("\t")[2]
			Cefazolin_result =line.split("\t")[3]
			#print(Cefazolin) #Cefazolin
			
		if line.startswith('"Cefepime"'):
			Cefepime_symbol =line.split("\t")[1]
			Cefepime_MIC =line.split("\t")[2]
			Cefepime_result =line.split("\t")[3]
			#print(Cefepime) #Cefepime
			
		if line.startswith('"Cefotaxime"'):
			Cefotaxime_symbol =line.split("\t")[1]
			Cefotaxime_MIC =line.split("\t")[2]
			Cefotaxime_result =line.split("\t")[3]
			#print(Cefotaxime) #Cefotaxime
			
		if line.startswith('"Cefotaxime/clavulanic acid"'):
			Cefotaxime_clavulanic_acid_symbol=line.split("\t")[1]
			Cefotaxime_clavulanic_acid_MIC=line.split("\t")[2]
			Cefotaxime_clavulanic_acid_result=line.split("\t")[3]
			#print(Cefotaxime_clavulanic_acid) #Cefotaxime_clavulanic acid
		
		if line.startswith('"Ceftazidime/clavulanic acid"'):
			Ceftazidime_clavulanic_acid_symbol =line.split("\t")[1]
			Ceftazidime_clavulanic_acid_MIC =line.split("\t")[2]
			Ceftazidime_clavulanic_acid_result =line.split("\t")[3]
			#print(Ceftazidime_clavulanic_acid) #Ceftazidime_clavulanic_acid
			
		if line.startswith('"Cefuroxime (sodium)"'):
			Cefuroxime_sodium_symbol =line.split("\t")[1]
			Cefuroxime_sodium_MIC =line.split("\t")[2]
			Cefuroxime_sodium_result =line.split("\t")[3]
			#print(Cefuroxime_sodium) #Cefuroxime_sodium
		
		if line.startswith('"Ciprofloxacin"'):
			Ciprofloxacin_symbol =line.split("\t")[1]
			Ciprofloxacin_MIC =line.split("\t")[2]
			Ciprofloxacin_result =line.split("\t")[3]
			#print(Ciprofloxacin) #Ciprofloxacin
		
		if line.startswith('"Colistin"'):
			Colistin_symbol =line.split("\t")[1]
			Colistin_MIC =line.split("\t")[2]
			Colistin_result =line.split("\t")[3]
			#print(Colistin) #Colistin
			
		if line.startswith('"Ertapenem"'):
			Ertapenem_symbol =line.split("\t")[1]
			Ertapenem_MIC =line.split("\t")[2]
			Ertapenem_result =line.split("\t")[3]
			#print(Ertapenem) #Ertapenem
			
		if line.startswith('"Fosfomycin + Glucose6Phosphate"'):
			Fosfomycin_Glucose6Phosphate_symbol =line.split("\t")[1]
			Fosfomycin_Glucose6Phosphate_MIC =line.split("\t")[2]
			Fosfomycin_Glucose6Phosphate_result =line.split("\t")[3]
			#print(Fosfomycin_Glucose6Phosphate) #Fosfomycin_Glucose6Phosphate
		
		if line.startswith('"Gentamicin"'):
			Gentamicin_symbol =line.split("\t")[1]
			Gentamicin_MIC =line.split("\t")[2]
			Gentamicin_result =line.split("\t")[3]
			#print(Gentamicin) #Gentamicin
			
		if line.startswith('"Levofloxacin"'):
			Levofloxacin_symbol =line.split("\t")[1]
			Levofloxacin_MIC =line.split("\t")[2]
			Levofloxacin_result =line.split("\t")[3]
			#print(Levofloxacin) #Levofloxacin
			
		if line.startswith('"Meropenem"'):
			Meropenem_symbol =line.split("\t")[1]
			Meropenem_MIC =line.split("\t")[2]
			Meropenem_result =line.split("\t")[3]
			#print(Meropenem) #Meropenem	
		
		if line.startswith('"Nitrofurantoin"'):
			Nitrofurantoin_symbol =line.split("\t")[1]
			Nitrofurantoin_MIC =line.split("\t")[2]
			Nitrofurantoin_result =line.split("\t")[3]
			#print(Nitrofurantoin) #Nitrofurantoin
			
		if line.startswith('"Piperacillin/Tazobactam"'):
			Piperacillin_Tazobactam_symbol =line.split("\t")[1]
			Piperacillin_Tazobactam_MIC =line.split("\t")[2]
			Piperacillin_Tazobactam_result =line.split("\t")[3]
			#print(Piperacillin_Tazobactam) #Piperacillin_Tazobactam
			
		if line.startswith('"Tigecycline"'):
			Tigecycline_symbol =line.split("\t")[1]
			Tigecycline_MIC =line.split("\t")[2]
			Tigecycline_result =line.split("\t")[3]
			#print(Tigecycline) #Tigecycline
			
		if line.startswith('"Tobramycin"'):
			Tobramycin_symbol =line.split("\t")[1]
			Tobramycin_MIC =line.split("\t")[2]
			Tobramycin_result =line.split("\t")[3]
			#print(Tobramycin) #Tobramycin
			
		if line.startswith('"Trimethoprim/Sulfamethoxazole"'):
			Trimethoprim_Sulfamethoxazole_symbol =line.split("\t")[1]
			Trimethoprim_Sulfamethoxazole_MIC =line.split("\t")[2]
			Trimethoprim_Sulfamethoxazole_result =line.split("\t")[3]
			#print(Trimethoprim_Sulfamethoxazole) #Trimethoprim_Sulfamethoxazole
		
			
			print(ID,source,org,
			Amikacin_symbol, Amikacin_MIC, Amikacin_result,
			Ampicillin_symbol, Ampicillin_MIC, Ampicillin_result,
			Ampicillin_Sulbactam_symbol, Ampicillin_Sulbactam_MIC, Ampicillin_Sulbactam_result,
			Aztreonam_symbol, Aztreonam_MIC, Aztreonam_result,
			Cefazolin_symbol, Cefazolin_MIC, Cefazolin_result,
			Cefepime_symbol,Cefepime_MIC, Cefepime_result,
			Cefotaxime_symbol, Cefotaxime_MIC, Cefotaxime_result,
			Cefotaxime_clavulanic_acid_symbol, Cefotaxime_clavulanic_acid_MIC, Cefotaxime_clavulanic_acid_result,
			Ceftazidime_clavulanic_acid_symbol,Ceftazidime_clavulanic_acid_MIC, Ceftazidime_clavulanic_acid_result,
			Cefuroxime_sodium_symbol,Cefuroxime_sodium_MIC, Cefuroxime_sodium_result,
			Ciprofloxacin_symbol,Ciprofloxacin_MIC, Ciprofloxacin_result,
			Colistin_symbol,Colistin_MIC, Colistin_result,
			Ertapenem_symbol,Ertapenem_MIC, Ertapenem_result,
			Fosfomycin_Glucose6Phosphate_symbol, Fosfomycin_Glucose6Phosphate_MIC, Fosfomycin_Glucose6Phosphate_result,
			Gentamicin_symbol, Gentamicin_MIC,Gentamicin_result,
			Levofloxacin_symbol, Levofloxacin_MIC, Levofloxacin_result, 
			Meropenem_symbol, Meropenem_MIC, Meropenem_result, 
			Nitrofurantoin_symbol, Nitrofurantoin_MIC, Nitrofurantoin_result,
			Piperacillin_Tazobactam_symbol, Piperacillin_Tazobactam_MIC, Piperacillin_Tazobactam_result,
			Tigecycline_symbol, Tigecycline_MIC, Tigecycline_result,
			Tobramycin_symbol, Tobramycin_MIC, Tobramycin_result,
			Trimethoprim_Sulfamethoxazole_symbol, Trimethoprim_Sulfamethoxazole_MIC,Trimethoprim_Sulfamethoxazole_result,
			 sep="\t", file=outfile)
			 
			
			
		
outfile.close()
infile.close()