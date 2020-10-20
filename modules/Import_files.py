# Importing tools 

from zipfile import ZipFile
from Bio import SeqIO

# For opening zip file for seq traces 
def process_zip(my_zip):
	with ZipFile(my_zip,'r') as seqtraces:
		seqtraces.extractall()
		l_filenames = seqtraces.namelist()
	return l_filenames

# Opening sequence and genebank file by calling name, can change the names to match input file name
# templateseq = SeqIO.read('pIO2_copy.gb','genbank' )

def seq_gen(my_fnames):
	for f in my_fnames:
		trace = SeqIO.read(f, 'abi')
		yield trace

def template_seq(filename, filetype):
	template = SeqIO.read(filename,filetype)
	templateseq = template.seq
	return templateseq


###### Example usage:
my_filenames = process_zip('/Users/izaiahornelas/Desktop/GitHub/SAShihME/SAShihMe/tests/test_zip_from_genewiz.zip')
my_seq_gen = seq_gen(my_filenames)
# Can iterate through generator once
for seq in my_seq_gen:
    print(seq.name, "\n", str(seq.seq.reverse_complement())[10:30], "\n")

# Ways to store generator result in memory:
# First re-init generator
my_seq_gen = seq_gen(my_filenames)
# store in variable using next()
first_seq = next(my_seq_gen)
second_seq = next(my_seq_gen)

# or store everything in list
my_seq_gen = seq_gen(my_filenames)
my_seq_list = list(my_seq_gen)
print(my_seq_list)