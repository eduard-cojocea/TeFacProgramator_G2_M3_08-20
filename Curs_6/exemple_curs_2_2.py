filename = "scipio.txt"
my_file = open(filename, "r")
count = 1
data = my_file.readline()
while data:
    print("line {}: {}".format(count, data), end="")
    count += 1
    data = my_file.readline()
my_file.close()