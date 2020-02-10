f = open("File_listt.txt","w")

list1 = [1,2,3,4,5,6]

#f.write(str(list1))

for i in list1:
    f.write(str(i)+"\n")


f.close()
