#check disk capacity on flux
df -h | grep "snitkin"

# rename all files with a different suffix in directory
rename .fna .fasta *.fna

# swap out characters 
# replace space with underscore
sed 's, ,_,g' -i GC*

# count all times a character occurs in a file
grep -c "^>" all_eclo.txt

#search recursively for a type of file and move them to a different directory
shopt -s globstar
cp **/*.gbk destination_dir

# do something to every file in a directory

for file in /dir/*
do
  cmd [option] "$file"
done

# FASTq to FASTA

sed -n '1~4s/^@/>/p;2~4p' in.fastq > out.fasta

