def arithmatic_operations(func):
	def operators(a, b):
		func(a, b)
		print("\nThe below operations are from decorator function : ")
		print("The product is : ", a*b)
		print("The division is : ", a/b)
		print("The remainder is : ", a%b)
	return operators

@arithmatic_operations
def add_and_subtract(a, b):
	print("The addition is : ", a+b)
	print("The subtraction is : ", a-b)

add_and_subtract(10,5)
