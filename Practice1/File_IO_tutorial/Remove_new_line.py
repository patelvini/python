# Python program to remove newline characters from a file.

f = open("File1.txt","r")
f_list = f.readlines()

def func(f_list):
    return [s.rstrip('\n') for s in f_list]

print(func(f_list))

f.close()
