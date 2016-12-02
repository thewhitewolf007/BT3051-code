# Homework header as usual
#
#
#
import sys
def read_fasta(fname):
    """ (str) -> (list of tuples)
    # function body with documentation

    """

    return sequences # a list of (sequence_name, sequence) tuples

def compute_protein_mass(protein_str):
    """
    #function body including documentation and test cases
    >>> compute_protein_mass('SKADYEK')
    821.392
    """

if __name__ == '__main__':
    #DO NOT CHANGE THE FOLLOWING STATEMENTS
    for seq_name, seq in read_fasta("hw1a_dataset.faa"):
        print (seq_name, compute_protein_mass(seq))