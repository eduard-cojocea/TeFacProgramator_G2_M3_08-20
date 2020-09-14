x=54332
copie = x
nr_cifre = 0

while copie != 0:
    print(copie)
    nr_cifre += 1
    copie //= 10
    
print("{} are {} cifre".format(x, nr_cifre))