# Program to append text to a file


# try:

f = open("File1.txt","a")
	# f = open("File1.txt","r")


string_input = input("Enter content for append in file : ")

f.write(string_input + "\n")

f.close()

f = open("File1.txt","r")

print(f.read())

f.close()
# except:

# 	print("FileNotFound Exception !!!")
