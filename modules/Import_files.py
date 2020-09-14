# Importing tools 

from zipfile import ZipFile

# For opening zip file for seq traces 
with ZipFile('Traces.zip','r') as seqtraces:
	seqtraces.extractall()
	listoffilenames = seqtraces.namelist()
  
# can continue down this route if we elect to unzip files. Next step would be to choose which file(s) we want to align with 'templateseq' and filter for it


# Opening sequence and genebank file by calling name, can change the names to match input file name
templateseq = SeqIO.read('pIO2_copy.gb','genbank' )
expseq = SeqIO.read('pIO2.1-RB_Check2.ab1','abi')
