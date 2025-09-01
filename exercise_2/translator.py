
"""This function is called 'translator'.
It takes 1 argument, a DNA sequence 'seq' and uses a dictionary present inside the functon called 'codon_table', 
to return an animo acid sequence.

If there are gaps in the sequence, you will get an error message.
If there are incomplete codons in the sequence, you will also get an error message."""



def translator(seq):
    
    codon_table = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L","CTT": "L", "CTC": "L","CTA": "L",
        "CTG": "L", "ATT": "I", "ATC": "I", "ATA": "I", "ATG" : "M", "GTT": "V", "GTC": "V", "GTA": "V",
        "GTG": "V", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "CCT": "P", "CCC": "P",
        "CCA": "P", "CCG": "P", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCT": "A",
        "GCC": "A", "GCA": "A", "GCG": "A", "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*","CAT": "H",
        "CAC": "H", "CAA": "Q", "CAG": "Q", "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAT": "D",
        "GAC": "D", "GAA": "E", "GAG": "E", "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W", "CGT": "R",
        "CGC": "R", "CGA": "R", "CGG": "R", "AGT": "S","AGC": "S", "AGA": "R", "AGG": "R",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    

    if not isinstance(seq, str):
        raise TypeError ("The sequence must be a string!")
    

    i = 0
    amino_acid = []

    seq = seq.upper()                                      #To make all DNA sequences uppercase

    if " " in seq:
        return "There are gaps in the sequence!"              
    
    elif len(seq)%3 !=0:
        return "There are incomplete codons at the end of the sequence!"
    
    elif len(seq)%3 ==0:
        while i < len(seq):
            amino_acid.append(codon_table.get(seq[i:i+3]))
            i +=3
            
        return "".join(amino_acid)

if __name__ == "__main__":
    
    seq = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA" 
    

    print(translator(seq))
    










