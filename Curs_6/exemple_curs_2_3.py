filename = "scipio.txt"
my_file = open(filename, "r")
file_lines = my_file.readlines()
print("The file contains:\n{}".format(file_lines))

count = 1
for line in file_lines:
    print("line {}: {}".format(count, line), end="")
    count += 1
my_file.close()