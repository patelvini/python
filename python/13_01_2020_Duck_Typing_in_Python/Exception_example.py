def exception_func():
	"""exception handling in python"""
	try:
		f = open("exception_file.txt","r")
	except:
		# raise Exception ("FileNotFoundException")
		print("FileNotFoundException occurs while opening a file!!")
	else:
		print("File open successfully.")
	finally:
		print("Done!")

exception_func()

