def top(func):
	def wrapper(*args,**kwargs):
		print("1" * 1)
		func(*args, **kwargs)
		print("1" * 1)
	return wrapper

def middle(func):
	def wrapper(*args,**kwargs):
		print("2" * 2)
		func(*args, **kwargs)
		print("2" * 2)
	return wrapper

def bottom(func):
	def wrapper(*args,**kwargs):
		print("3" * 3)
		func(*args, **kwargs)
		print("3" * 3)
	return wrapper

@top
@middle
@bottom
def myTest(anyString):
	print(anyString)

myTest("Hello")