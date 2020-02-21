def Reverse_fun_1(s):
    return s[::-1]

def Reverse_fun_2(s):
    s1 = ""
    for i in s:
        s1 = i + s1
    return s1


str = input("Enter any string : ")

print("Using inbuilt function : ",Reverse_fun_1(str))
print("Using custom function :  ",Reverse_fun_2(str))
