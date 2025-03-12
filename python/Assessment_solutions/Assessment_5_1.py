N = int(input("Enter a number : "))

def recFun(N, n=0):
    print("*", end= " ")
    if n < N:
        recFun(N, n + 1)

recFun(N)