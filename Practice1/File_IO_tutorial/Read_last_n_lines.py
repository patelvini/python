# program to read last n lines

line_num = int(input("Enter line number : "))

line_count = 0

f = open("File1.txt","r")

for line in f:
	line_count += 1

	if line_count>line_num:
		print(line)

f.close()
  




