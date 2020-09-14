produs = lambda x, y: x*y

print(produs(3, 4))
print(produs(2.1, 3))
print(produs("Stefan", 3))

constant = lambda : 99

print(constant())

even = lambda x: x%2==0

print(even(2))
print(even(3))

numbers = [21.3, 45.2, 546.4352, 123.34, 434.432]

int_numbers = list(map(lambda x: int(x), numbers))
print(int_numbers)

even_numbers = list(filter(lambda x: x%2==0, int_numbers))
print(even_numbers)