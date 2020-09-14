def my_func(val1, val2, val3, *values):
    print("val1: {}\nval2: {}\nval3:{} \n".format(val1, val2, val3, values))
    for val in values:
        print(val, end="\n\n")
    print("="*100)
        
my_func(1, 2, 3)
my_func(1, 2, 3, 4)
my_func(1, 2, 3, 4, 5, 6, [98, 99, 100], 7, 8)

def my_func2(val1, val2, val3, values):
    print("val1: {}\nval2: {}\nval3:{} \n".format(val1, val2, val3, values))
    for val in values:
        print(val)
    print("="*100)
    
        
my_func2(1, 2, 3, ())
my_func2(1, 2, 3, (4,))
my_func2(1, 2, 3, (4, 5, 6, 7, 8))