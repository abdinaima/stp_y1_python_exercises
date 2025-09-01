
"""This module is called 'nucleotide_count'.
It takes 1 argument, a DNA sequence 'seq'.
The function 'single_nucleotide' counts the number of each base in a sequence.
The function 'di_nucleotide' counts the number of non-overlapping dinucleorides in a sequence.
The function 'tri_nucleotide' counts the number of non-overlapping trinucleotides in a sequence.
Each function returns the result as a dictionary"""


def single_nucleotide (seq):
    
    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    seq = seq.lower()

    counts = {}

    for i in range (len(seq)):
        nuc = seq[i]
        
        counts[nuc] = counts.get(nuc, 0) + 1

    return counts




def di_nucleotide (seq):

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    seq = seq.lower()

    counts = {}
    
    for i in range (0, len(seq)-1, 2):
        dinuc = seq[i:i+2]
        
        counts[dinuc] = counts.get(dinuc, 0) + 1
    
    return counts



def tri_nucleotide (seq):

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    seq = seq.lower()
    
    counts = {}
    
    for i in range (0, len(seq)-1, 3):
        trinuc = seq[i:i+3]
        
        counts[trinuc] = counts.get(trinuc, 0) + 1
    
    return counts



if __name__ == "__main__":
    

    seq = "aggagtaagcccttgcaactggaaatacacccattg"

    # seq = "GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA"


    print(single_nucleotide(seq))
    
    print(di_nucleotide(seq))

    print(tri_nucleotide(seq))
  


