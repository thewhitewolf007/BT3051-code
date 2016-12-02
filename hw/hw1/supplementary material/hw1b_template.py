# Homework header as usual
#
#
#
import doctest

def translate_DNA(mrna, translation_table = 'RNA_TABLE.txt'):
    """
    #function body including documentation and test cases
    >>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
    MYDATASTRCTRES
    """

if __name__ == '__main__':
    doctest.testmod(verbose = True)