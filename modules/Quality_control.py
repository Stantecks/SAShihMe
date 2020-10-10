from Bio.Seq import Seq 
from Bio import SeqIO

## Test with to following
# from Import_files import process_zip, seq_gen
# my_obj_lst = list(seq_gen(process_zip('../tests/test_zip_from_genewiz.zip')))
## input for my_seq must be a Seq() object such as my_obj_lst[0].seq

# for item in my_obj_lst:
#     print(seq_trim(10, item.seq), "\n\n")

def begin_slide(window_size, my_seq):
    start, end = 0, window_size
    assert window_size < len(my_seq), "Sequence should be longer than window_size"
    start_coord = None
    while end < len(my_seq) - window_size:
        frame = my_seq[start:end]
        N_ratio = 100* float(frame.count('N') / len(frame))
        if N_ratio <= 20:
            start_coord = start
        start += 1
        end += 1
        if start_coord:
            break
    assert start_coord, "No suitable window could be found"
    return start_coord

def end_slide(window_size, my_seq):
    rev_coord = begin_slide(window_size, my_seq.reverse_complement())
    assert rev_coord, "No suitable window could be found"
    return len(my_seq) - rev_coord

def seq_trim(window_size, my_seq):
    start = begin_slide(window_size, my_seq)
    end = end_slide(window_size, my_seq)
    return my_seq[start:end]