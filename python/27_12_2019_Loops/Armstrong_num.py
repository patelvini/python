num = int(input("Enter a number : "))
res = 0
n = len(str(num))
original_num = num

while original_num != 0:
    r = original_num % 10
    res += r ** n
    original_num //= 10

if res == num:
    print("Armstrong number")
else:
    print("Not Armstrong")