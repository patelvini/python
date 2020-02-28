
n = int(input("Enter a number : "))

def pattern(n,k):
    if n < 0 :
        return

    pattern(n-1,k+1)

    for i in range(0,k):
        print(" ", end = " ")

    for i in range(0,n):
        print("*",end = " ")
    print()

pattern(n,0)

