def top(func):
	def wrapper(*args, **kwargs):

		print("*" * num)
		func(*args, **kwargs)
		print("*" * num)
	return wrapper

@top
def myTest(num):
	print(num)

num = int(input("Enter a number : "))

myTest(num)


