from Bio.Seq import Seq 
from Bio import SeqIO

# Need to make a code where we taking reading frames of 10-mer and if there is an N, keep going
#seq2 = SeqIO.read('pIO11.1-RB_Check2.ab1','abi')    INSERT FILE HERE 
#just_seq2 = str(seq2.seq)
frame = 0 # need to define it first
fullread =[] # Creating list for clean frame
print (just_seq2)
while frame < len(just_seq2):
    readingframe = just_seq2[(frame):(frame+10)]
    frame = frame + 10
    NAGCT = 100* float(readingframe.count('N') / len(readingframe))
    print (readingframe, NAGCT)
    if NAGCT < 60:
        fullread.append(readingframe)
        fullcleanread = ''.join(fullread)
        print (fullcleanread)
