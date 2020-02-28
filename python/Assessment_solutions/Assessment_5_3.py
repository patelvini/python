N = int(input("Enter a number : "))

def recFun(N, n = N):
    print(n, end= " ")
    if n > 1 :
        recFun(N, n - 1)

recFun(N)