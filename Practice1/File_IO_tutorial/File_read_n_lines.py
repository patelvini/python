# # program to read first n line



n = int(input("Enter the no of lines for reading : "))
f = open("File1.txt","r")


def read_n_lines(f,n):
	try:
		num_lines = 0
		for line in f:
			if num_lines < n:
				print(line)
				num_lines += 1
	except:
		print("EOF Error !!")

read_n_lines(f,n)

f.close()




# alternative approach
 
# from itertools import islice

# def read_n_lines(f,n):
# 	for line in islice(f,n):
# 		print(line)

# read_n_lines(f,n)







