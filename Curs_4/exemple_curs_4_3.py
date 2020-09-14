def print_human(name, height, weight):
    print("name: {}\nheight: {}\n weight: {}".format(name, height, weight))
    
print_human("Stefan", 1.65, 70)
print_human(name="Stefan", weight=70, height=1.65)
print_human("Stefan", weight=70, height=1.65)
# Not workig. Positional arguments must not be after keyword argument
print_human(weight=70, "Stefan", height=1.65)
    
