# BT3051    Assignment 1b
#Roll Number: BE14B002
#Collaborators: BE14B020
#Time: 45:00
import doctest

def translate_DNA(mrna, translation_table = 'RNA_TABLE.txt'):
    """
    #function body including documentation and test cases
    >>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
    MYDATASTRCTRES
    >>> translate_DNA('AUGUA')
    The sequence is not a multiple of three.
    """
    if (len(mrna)%3!=0):
        print("The sequence is not a multiple of three.")
    else :
        with open(translation_table) as file:
            translate={}
            for lines in file:
                lines=lines.split()
                for itrans in range(0,len(lines),2):
                    translate[lines[itrans]]=lines[itrans+1]
        prot=''
        for irna in range(0,len(mrna),3):
            if(translate[mrna[irna:irna+3]] == "Stop"):
                break
            prot+=translate[mrna[irna:irna+3]]

        print(prot)

if __name__ == '__main__':
    doctest.testmod(verbose = True)
