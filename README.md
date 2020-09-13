# SAShihMe

- [ ] Genbank and ab1 file importing.
	- [ ] Should it be a zipped file of ab1 files and one genbank?
	- [ ] How should the filenames work?

- [ ] Quality control
	- [ ] Find a good inital cutoff number for sequencing reaction (might have to look at sequencing files)  Though we should be conservative (less things cut off)
	- [ ] Develop sliding window to check ratio of N:ATCG.  Also define window size.

- [ ] Pairwise Alignment.
	- [ ] Pairwise align a genbank plasmid with a arbitrary biopython sequence object.
	- [ ] Check to see if scoring will affect how alignments are done.
	- [ ] Find way to tabulate where mismatches and gaps are:  (start, end, what bases)

- [ ] Outputs (should be done last)
	- [ ] Generate a nice print statement that takes data from above and generates a feature specific report and a global report.
	- [ ] Experiment with different report styles.
