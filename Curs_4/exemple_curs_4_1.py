def suma(x, y):
    """Computes and returns the sum of two numbers.
    dsadasdasdas
    dsadsa
    dsa"""
    s = 0
    if type(x) is list:
        for val in x:
            s += val    
    if type(y) is list:
        for val in y:
            s += val
    if type(x) is int:
        s += x
    if type(y) is int:
        s += y
    return s
    
z = suma(4, 7)
print(z)
print(suma.__doc__)
z = suma([1,2,3], [5,6])
print(z)
z = suma([1,2,3], 100)
print(z)