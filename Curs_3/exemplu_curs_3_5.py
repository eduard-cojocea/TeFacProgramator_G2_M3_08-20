values = [1, 2, 3, 4, 5, 6, 7]
it = iter(values)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("starting the for")
for val in it:
    print(val)
