print("Hello world")
x = 10
if x > 0:
    x = x + 3
    x = x*4
    x = x - 1
    print("in if")

suma = 3 + 4 + \
        5 \
        + 8
        
# print(suma)

y = input("Introduceti valoarea lui y: ")
y = int(y)
square = y**2
print("Patratul lui y este: " + str(square))
prag = 10
if y > prag:
    print("%i este mai mare decat %i" % (y, prag))
    print(str(y) + " este mai mare decat " + str(prag))
    print("{1} este mai mare decat {0}".format(y, prag))
elif y > 0:
    print("y este mai mare decat 0 si mai mic decat 10")
else:
    print("y este mai mic decat 0")