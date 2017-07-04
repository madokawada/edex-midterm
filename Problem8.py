x = 10
result = 0

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    global x
    global result
    tempL = len(L)
    
    if tempL == 0:
        return result
    elif tempL > 0:
        for i in range(len(L)):
            result += L[i]*(x**(tempL-1))
        return general_poly (L[0:-1])
        

general_poly([1, 2, 3, 4])








#    i = 0
#    total = 0
#    if i < len(L):
#        total += L[i]*(10 ** (len(L)-i-1))
#        i += 1
#    else:
#        return total