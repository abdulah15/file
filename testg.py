file = open('example.txt','r')
print(file.read())
file.close()

file = open('example.txt','w')
file.write("hi")
file.close()

file = open('example.txt','a')
file.write("hello")
file.close()

