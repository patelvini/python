f = open("file_with_special_char.txt", "a+")

f.write("Hello vini \n")
f.write("Hello python\n")
f.write("Hello@123$%^")

f.seek(0)
l = ['!','@','#','$','%','^','&','*']
l1=f.read()
print(l1)

for i in l1:
    if i in l:
        print(i,end=" ")
