def my_func(x, y):
    s = x+y
    p = x*y
    d = x/y
    return s, p, d
    
print(my_func(2, 3))
suma, produs, diviziune = my_func(4, 5)
print(suma)
print(produs)
print(diviziune)