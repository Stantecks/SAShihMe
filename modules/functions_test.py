from Quality_control import begin_slide, end_slide, seq_trim
from Import_files import process_zip, seq_gen

def test_zipQC():
    l_files = process_zip('tests/test_zip_from_genewiz.zip')
    assert len(l_files) == 4

    my_gen = seq_gen(l_files)
    trimmed_lens = [len(seq_trim(10, my_obj.seq)) for my_obj in my_gen]

    my_gen = seq_gen(l_files)
    my_lens = [len(my_obj.seq) for my_obj in my_gen]

    for trimmed, original in zip(trimmed_lens, my_lens):
        assert trimmed <= original