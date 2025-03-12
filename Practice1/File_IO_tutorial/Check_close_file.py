# Write a Python program to assess if a file is closed or not.


f = open("File1.txt","r")

f.close()

try:
    f.write("Hello")
    print("File is not closed yet.")
except:
    print("File is closed")
