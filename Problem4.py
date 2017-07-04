def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i = 0
    total = 0
    while total < k:
        total += (i + 1)
        i += 1
    if total == k:
        return True
    else:
        return False
        
is_triangular(15)
        
    