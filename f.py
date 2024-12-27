f1 =input("Enter the name of the first file")
f2 = input("Enter the name of the second file")

f1 = open(f1, "r")
f2 = open(f2, "r")

print('content of the first file before appending -\n',f1.read())
print('content of the second file before appending -\n',f2.read())

f1.close()
f2.close()