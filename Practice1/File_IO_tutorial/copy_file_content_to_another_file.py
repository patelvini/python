f1 = open("File1.txt","r")
f2 = open("File2.txt","w")

f2.write(f1.read())

f1.close()
f2.close()

# alternative

from shutil import copyfile

copyfile("File1.txt","File2.txt")
