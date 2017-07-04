d = {1:10, 2:20, 3:30}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Swap keys and values
    dTemp = {val:key for (key, val) in d.items()}
    
    # Create a list to place the dictionary values in
    dictionaryValues = []

    # For each key in the dictionary's Values,
    for x in dTemp.values():
        # add the key to dictionaryValues
        dictionaryValues.append(x)

    
    print (dTemp)
    
dict_invert(d)