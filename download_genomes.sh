 #!/bin/sh 
 
 # SHELL SCRIPT TO DOWNLOAD .gbff.gz FILES FOR SPECIFIED
 # GENOMES FROM THE NCBI GENBANK DATABASE.
 # WRITTEN BY SHAWN WHITEFIELD 7-9-2015
 
 # TO RUN: ./download_genomes.sh genus_species species_label 
 
# SETUP GENUS_SPECIES & GENOME GENBANK FILE SUFFIX VARIABLES

genus_species=$1
species_label=$2 
genbank_ext='/*_genomic.gbff.gz'
genbank_label='.gbff_files'

#DOWNLOAD APPROPRIATE ASSEMBLY_SUMMARY.TXT FILE FROM NCBI
 
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/$1/assembly_summary.txt
 
# RENAME ASSEMBLY_SUMMARY.TXT WITH TODAY'S DATE AND SPECIES

assembly_summary='_assembly_summary.txt'
assembly_name=$(date +"%m_%d_%Y_")$1$assembly_summary  
mv assembly_summary.txt ./$assembly_name
 
#PARSE THE ASSEMBLY_SUMMARY.TXT FILE
# need fields: 20 = link to directory

cut -f 20 ./$assembly_name > strain_link.txt

# DOWNLOAD ALL OF THE GENOME.GBFF.GZ FILES FOR EACH LINE IN THE SUMMARY.TXT FILE
# NOTE: CAN CHANGE  genbank_ext to get any file type 

while read strains; do
	wget $strains$genbank_ext
done <strain_link.txt
 
# MOVE ALL OF THE .GBFF.GZ FILES TO A NEW DIRECTORY

mkdir $(date +"%m_%d_%Y_")$1$genbank_label
mv *.gz ./$(date +"%m_%d_%Y_")$1$genbank_label
cd ./$(date +"%m_%d_%Y_")$1$genbank_label
 
#RENAME THE FILES LIKE: eclo_<strain>.gb.gz
rename .gbff.gz .gb.gz *.gbff.gz

for file in *.gz; do
mv $file $2'_'$file
done
	

# GET REFERENCES FOR STRAINS

zcat * | grep PUBMED > $(date +"%m_%d_%Y_")"PUBMED_IDs.txt"

# PRINT HOW MANY GENOMES WERE DOWNLOADED

echo "Congrats, you have downloaded $(ls -l | wc -l) $1 genbank files"



#DONE


