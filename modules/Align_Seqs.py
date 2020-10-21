# Call tools 
from Bio import SeqIO
from Bio import pairwise2 
from Bio.Seq import Seq
from Quality_control import begin_slide, end_slide, seq_trim
from Import_files import process_zip, seq_gen, template_seq
from Bio.pairwise2 import format_alignment

# Starting with importing files (doing one by one)
my_filenames = process_zip('/Users/izaiahornelas/Desktop/GitHub/SAShihME/SAShihMe/tests/test_zip_from_genewiz.zip')
my_gen = seq_gen(my_filenames)
first_seq = next(my_gen)
firstseq = first_seq.seq

# my_seq_list = list(my_gen) #turning into list
# trimmed_seq = [len(seq_trim(10, my_obj.seq)) for my_obj in my_seq_list] # trimming seq 

# Loading template 
templateseq = template_seq('/Users/izaiahornelas/Desktop/GitHub/SAShihME/SAShihMe/tests/pIO11.gb','genbank')


# Aligning seqs
#alignments = pairwise2.align.globalxx(templateseq,firstseq)
#for alignment in alignments:
#     print(format_alignment(*alignment))