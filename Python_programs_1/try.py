def collect_vowels(s):
    '''
    (str) -> str

    Return a string containing the vowels in given string.
    
    >>> collect_vowels('This is neha hanamsagar')
    'iieaaaaa'
    >>> collect_vowels('xyz')
    ' '
    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels += char
    return vowels        




def count_vowels(s):
    '''
    (str) -> int
    
    Return the number of vowels is the given string. 

    >>> count_vowels("This is Neha Hanamsagar")
    8
    >>> count_vowels('xyz')
    0
    '''
    count_vowels = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count_vowels += 1
    return count_vowels

            
