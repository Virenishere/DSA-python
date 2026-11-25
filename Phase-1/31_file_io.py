# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# st = "Hey Viren you are amazing"
# f = open("myFile.txt", "w")
# f.write(st)
# f.close()


f = open("file.txt")

# whole para 
# lines = f.readlines()
# print(lines, type(list))

# read by line
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# f.close()


# the same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# you dont have to explicity close the file 