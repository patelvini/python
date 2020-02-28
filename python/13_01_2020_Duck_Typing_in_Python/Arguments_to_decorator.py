def argument_for_decorator(arg1,arg2):
	def decorator(func):
		def wrapper(*args):
			print("\n%s %s" %(arg1,arg2))
			func(*args)
		return wrapper
	return decorator

@argument_for_decorator("Hello","World!")
def print_func(*args):
	for i in args:
		print(i, end = " ")

print_func(1,2,3,4,5,6,7,8)