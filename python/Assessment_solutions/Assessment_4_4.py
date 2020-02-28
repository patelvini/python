s = input("Enter a string : ")
n = int(input("Enter position to remove one character : "))


def fun_remove(s, n):
    s1 = ""
   # s1 = s[0:n] + s[n + 1:len(s)]  # Alternative way
    for i in range(0,len(s)):
        if i != n:
            s1=s1+s[i]
    print(s1)


fun_remove(s, n)