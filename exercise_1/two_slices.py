"""This function is called 'two_slices'.
It takes 4 arguments: a DNA sequence 'seq' and two pairs of integers.
The first pair of integers is defined by 'n1' and 'n2'.
The second pair of integers is defined by 'n3' and 'n4'.
The function returns 2 slices of the DNA sequence, between the positions represented by the two number pairs inclusively"""


def two_slices (seq, n1, n2, n3, n4):
    print(f"{seq[n1:n2]} {seq[n3:n4]}")
    

if __name__ == "__main__":
    two_slices("""GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAG
GAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCT
TCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTC
TGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTG
AAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAG
GAGCCTACAAGAAAGTACGAGATTTGAT""", 137, 143, 274, 280)

