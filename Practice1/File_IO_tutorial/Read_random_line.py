 # Python program to read a random line from a file

 
import random

f1 = open("File1.txt","r")

lines = f1.read().splitlines()

print(random.choice(lines))

f1.close()
