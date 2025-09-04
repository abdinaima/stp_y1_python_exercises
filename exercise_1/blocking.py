
"""This function is called 'blocking'.
It takes 2 arguments, a DNA sequence 'seq' and an integer 'blocksize'.
The function then prints the sequence in blocks of the desired size, with gaps seperating the blocks."""


def blocking (seq, blocksize):

    seq = seq.upper()

    allowed_bases = {"A", "T", "C", "G"}

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    for x in seq:
        if x not in allowed_bases:
            raise ValueError ("Invalid non-DNA bases appear in this sequence!")

    if not isinstance(blocksize, int) or blocksize <= 0:
        raise ValueError ("The blocksize must be a positive integer!")
    
    
    
    i = 0
    blocks = []

    while i < len(seq):
        blocks.append(seq[i:i+blocksize])
        i +=blocksize
    
    return " ".join(blocks)

if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    
    blocksize = 10

    print(blocking(seq, blocksize))

