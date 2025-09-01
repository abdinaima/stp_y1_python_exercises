
"""This function is called 'GC_content'.
It takes 1 argument, a DNA sequence 'seq', and returns the percentage of "G" and "C" bases in a sequence, to 2 d.p."""


def GC_content(seq):

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    

    seq = seq.upper()                                    #To make all nucleotides upper case

    G_count = seq.count("G")
    C_count = seq.count("C")

    length = len(seq)

    return round((G_count + C_count)/length * 100, 2)

if __name__ == "__main__":
    
    seq = """GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAG
GCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGT
TGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGA
TCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAAC
CAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAG
TACGAGATTTGAT"""
    
    print(GC_content(seq))