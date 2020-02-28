n = int(input("Enter a number : "))

def prime(n):
	flag = 0
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				flag = 1
	if n == 1:
		return "It is coposite number"

	if flag == 1:
		return "Not prime"
	else:
		return "Prime"

x=prime(n)
print(x)

