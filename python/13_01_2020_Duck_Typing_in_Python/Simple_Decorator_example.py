def decorate(func):
	def first():
		print("This is the first program on decorators.")
		func()
	return first

def not_decorated():
	print("Hello from not decorated function\n")

@decorate
def hello():
	print("Hello from decorated function")

not_decorated()
hello()

