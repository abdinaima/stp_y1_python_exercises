
"""This module is called 'reverse_complement'.
It takes 1 argument, a DNA sequence 'seq' and has separate functions that return the reverse, complementary and reverse complementary sequence. 
Each of these functions are seperated and can be reused."""


def reverse(seq):

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")

    return seq[::-1]


def complement(seq):
    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    return seq.translate(str.maketrans("atcgATCG", "tagcTAGC"))


def reverse_complement(seq):
    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    return complement(reverse(seq))



if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"""
    
    print(reverse_complement(seq))