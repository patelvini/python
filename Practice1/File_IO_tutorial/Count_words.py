# Python program that takes a text file as input and returns the number of words of a given text file
# Note: Some words can be separated by a comma with no space.

f = open("File1.txt","r")

str1 = f.read().replace(","," ")

f_list = str1.split()

print("Total no. of words : ",len(f_list))

f.close()
