s = input("Enter a string : ")

def Find_Average(s):
    l1 = list(s)
    sum = 0
    for i in l1:
        sum = sum + ord(i)
    return sum/len(l1)

print(Find_Average(s))