
"""This function is called 'blocking'.
It takes 2 arguments, a DNA sequence 'seq' and an integer 'blocksize'.
The function then prints the sequence in blocks of the desired size, with gaps seperating the blocks."""


def blocking (seq, blocksize):

    i = 0
    blocks = []

    while i < len(seq):
        blocks.append(seq[i:i+blocksize])
        i +=blocksize
    
    print(" ".join(blocks))

if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    blocksize = 10

    blocking(seq, blocksize)

