n = input("Enter a string : ")
# n2 = ''.join(reversed(n))
n2 = n[::-1]
if n == n2:
    print("Palindrom")
else:
    print("Not palindrom")