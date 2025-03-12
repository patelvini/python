def no_ones(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count

def display(list1):
    for i in list1:
        x = no_ones(i)
        if x % 2 == 0:
            list2.append(i)
    print(list2)

list1, list2 = [], []

n1 = int(input("Enter len of list : "))

for i in range(0,n1):
    list1.append(int(input("Enter list element : ")))

display(list1)

