# BT3051    Assignment 1b
#Roll Number: BE14B002
#Collaborators: BE14B020
#Time: 1:30
import sys
import doctest
def read_fasta(fname):
    """ (str) -> (list of tuples)
    # function body with documentation
    """
    seq=[]
    sequence_name=[]
    sequence=[]
    with open(fname) as file:
        lines=file.read()
        lines=lines.split(">")
        lines = list(filter(None, lines))
        for iseq in lines:
            seq.append(iseq.split("\n"))
        for ilist in seq:
            sequence_name.append(ilist[0])
            sequence.append("".join(ilist[1:len(ilist)]))
        sequences=list(zip(sequence_name,sequence))
    return sequences # a list of (sequence_name, sequence) tuples

def compute_protein_mass(protein_str):
    """
    (str)->(float)
    #function body including documentation and test cases
    >>> compute_protein_mass('SKADYEK')
    839.407
    """
    with open("PROT_MASS.txt") as file:
        weights={'X':0}
        mass=0
        for lines in file:
            lines=lines.split()
            weights[lines[0]]=float(lines[1])
    for ilet in protein_str:
        mass+=weights[ilet]
    mass+=18.01528
    mass=float("%.3f" %mass)
    return mass

if __name__ == '__main__':
    #DO NOT CHANGE THE FOLLOWING STATEMENTS
    for seq_name, seq in read_fasta("hw1a_dataset.faa"):
        print (seq_name, compute_protein_mass(seq))

if __name__ == '__main__':
    doctest.testmod(verbose = True)
