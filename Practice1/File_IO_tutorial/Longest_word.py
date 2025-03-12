# program to find longest word from a file

f = open("File1.txt","r")

words = f.read().split()
length = 0
x=[]
for word in words:
	if len(word)==length:
		length = len(word)
		x.append(word)
	elif len(word)>length:
		x.clear()
		x.append(word)
		length = len(word)

print(length)
print(x)