import MarvellousNum_3_5

def ListPrime(n):
    for i in range(0,n):
        l1.append(int(input("Enter element of list : ")))
    print(l1)
    for i in l1:
        n1 = MarvellousNum_3_5.ChkPrime(i)
        if n1 == 0 :
            l2.append(i)
    return sum(l2)


n = int(input("Enter no of elements : "))
l1,l2=[],[]
print(ListPrime(n))

