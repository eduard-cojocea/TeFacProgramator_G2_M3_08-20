from math import sqrt

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1 )):
        if x % i == 0:
            return False
    return True
    
values = list(range(100))

for val in values:
    if not is_prime(val):
        continue
    print(val)
    
    
def compress_image():
    pass
    
print(compress_image())