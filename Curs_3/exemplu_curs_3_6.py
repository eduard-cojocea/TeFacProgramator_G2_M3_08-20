names = ["Stefan", "Edi", "Scipio"]
heights = [1.5, 1.9, 1.7]

zipped = zip(names, heights)

#print("zipped:")
#print(list(zipped))

unzipped = zip(*zipped)

print("unzipped")
print(list(unzipped))
print(list(unzipped))

# n = list(unzipped)[0]
# h = list(unzipped)[1]

#print(n, h)

