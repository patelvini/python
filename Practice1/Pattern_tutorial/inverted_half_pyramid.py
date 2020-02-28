n = int(input("Enter a Number : "))

def row_pattern_func(n):
    if n<1:
        return
    print(n,end = " ")
    row_pattern_func(n-1)

def pattern_func(n):
    if n<1:
        return
    row_pattern_func(n)
    print()
    pattern_func(n-1)

pattern_func(n)
