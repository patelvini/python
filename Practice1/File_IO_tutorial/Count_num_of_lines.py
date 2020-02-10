# Python program to count the number of lines in a text file.

f = open("File1.txt","r")

count = 0

for i in f:
	count += 1

print("No. of line in file : ",count)