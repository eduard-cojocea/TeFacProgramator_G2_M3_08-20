filename = "scipio.txt"
my_file = open(filename, "r")
data = my_file.read()
print("The file contains:\n{}".format(data))
my_file.close()

print("*"*100)

my_file = open(filename, "r")
data = my_file.read(40)
print("The file contains:\n{}".format(data))
my_file.close()