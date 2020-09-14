filename = "scipio.txt"
my_file = open(filename, "r")
data = my_file.read(25)
print("The first 25 bytes are:\n{}".format(data))
print("The cursor is at position: {}".format(my_file.tell()))
my_file.seek(10, 0)
print("The cursor is at position: {}".format(my_file.tell()))

data = my_file.read(15)
print("The bytes from position 10 to position 25 are:\n{}".format(data))
print("The cursor is at position: {}".format(my_file.tell()))
my_file.close()