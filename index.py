with open("sample_doc.txt", "w") as f:
    f.write("hi there")


with open("sample_doc.txt", "r") as f:

    data = f.readlines()
print("words in the file are ")
for line in data :
    word = line.split()
    print(word)


f.close()