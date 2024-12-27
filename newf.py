newfile = open('File.txt','x',)
newfile.close()

import os 
print("check if file exist or not")
if os.path.exists('File.txt'):
    print("File exists")
else:
    print("File does not exist")

os.remove('File.txt')
os.rmdir('op')