n = int(input("Enter a number : "))

def row_pattern(n):
    if n > 0:
        row_pattern(n-1)
        print(n, end = " ")

def pattern(n):
    if n > 0:
        pattern(n-1)
    row_pattern(n)
    print()

pattern(n)

