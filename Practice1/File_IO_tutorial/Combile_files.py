f1 = open("File1.txt","r")

f2 = open("teest.txt","r")

for l1,l2 in zip(f1,f2):
    print(l1,":",l2)

f1.close()
f2.close()
