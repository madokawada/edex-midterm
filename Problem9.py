L1 = ['a', 'a', 'b']
L2 = ['a', 'b']

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    for char in L:
        if char in L2:
            del(char)
    
is_list_permutation(L1, L2)