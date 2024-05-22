#!/usr/bin/env python




#import biopython modules for blasting and parsing blast output

from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#LOOP TO DO THE BLASTING WITH EVERY GENOME IN DIRECTORY AS A QUERY
...

#1 genome for now...

blastx_cline = NcbiblastxCommandline(query="/nfs/esnitkin/Shawn/UM_CRE-1/UM-CRE_fasta/genome_fasta/genomes/UM-CRE-1-1_S2_L001_R1_l500_contigs.fasta", db="one_porin.fasta", evalue=0.001,outfmt=5, out="./test_porins.xml")
stdout, stderr = blastx_cline()

#PARSE THE BLAST OUTPUT
#can only step through result_handle 1 time

result_handle = open("test_porins.xml")
blast_records = NCBIXML.parse(result_handle) #iterator for multiple objects
for blast_record in blast_records:
	print(blast_record.matrix)

	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			print('*****Alignment*****')
			print('sequence:', alignment.title)
			print('length:', alignment.length)
			print('e value:', hsp.expect)
			print('hsp score', hsp.score)
			print('identities', hsp.identities)
			print(hsp.query)
			print(hsp.match)
			print(hsp.sbjct)



for Parameters in blast_records:
	for parameter in blast_record.Parameters:
		print(parameter.effective_hsp_length)
		
		
		
result_handle = open("test_porins.xml")
blast_records = NCBIXML.parse(result_handle) #iterator for multiple objects
for blast_record in blast_records:
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			print('*****Alignment*****')
			print('sequence:', alignment.title)
			print('length:', alignment.length)
			print('e value:', hsp.expect)
			print('hsp score', hsp.score)
			print('identities', hsp.identities)
			print(hsp.query)
			print(hsp.match)
			print(hsp.sbjct)