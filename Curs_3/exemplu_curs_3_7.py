data = ["Stefan", 1, 2, 3, 4, 5, "Edi", 6, 7, 8, 9, 10]

result = list(zip(*[(iter(data))]*6))

print(result[0])
print(result[1])
print(list(zip(*result)))