def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_of_nucleotide = 0
    for a in dna:
        if nucleotide == a:
            count_of_nucleotide += 1
            
    return count_of_nucleotide


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> boolean

    Return True if and only if given string contains no characters other than 'A','C','T','G'
    >>>is_valid_sequence("ACTGHJ")
    False
    >>>is_valid_sequence("ACTG")
    True
    """
    boo = []
    
    for c in dna:
        if c in "ACTG":
            boo += "T"
        else:
            boo += "F"
    return "F" not in boo         

def insert_sequence(dna1,dna2,index):
    """(str, str, int) -> str
    Return the dna sequence by adding the second dna sequence in the first dna sequence at the given index.
    >>>insert_sequence("ACTGGGAC", "GG",2)
    "ACGGTGGGAC"
       
    """
    return dna1[:index]+dna2+dna1[index:]

def get_complement(dna):
    """ (str) -> (str)

    Return the dna's nucleotide's complement.
    complements are- A and T , C and G
    >>>get_complement("ACT")
    "TGA"
    
    """
    d = {"A":"T", "T":"A", "C":"G", "G":"C"}
    dna1 = ""
    for c in dna:
        dna1 += d[c]
    return dna1    
        
        
            
    
