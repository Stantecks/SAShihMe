# Call tools 
from Bio import SeqIO
from Bio import pairwise2 
from Bio.Seq import Seq
from Quality_control import begin_slide, end_slide, seq_trim
from Import_files import process_zip, seq_gen

# Starting with importing files (doing one by one)
my_filenames = process_zip('/SAShihMe/tests/test_zip_from_genewiz.zip')
my_seq_gen = seq_gen(my_filenames)
