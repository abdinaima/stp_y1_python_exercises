
"""This function is called 'transcriber'.
It takes 1 argument, a DNA sequence 'dna', and transcribes it by replacing the t (or T) with u (or U).
It returns an RNA sequence 'rna', which can then be used later (e.g. in a later function)"""


def transcriber (dna):
    
    if not isinstance(dna, str):
        raise TypeError ("The sequence must be a string!")

    return dna.translate(str.maketrans("tT", "uU"))


if __name__ == "__main__":
    
    dna = """GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"""
    
    rna = transcriber(dna)
    
    print(rna)