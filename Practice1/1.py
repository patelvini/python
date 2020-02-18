class ShortInputException(Exception):
	'''A user-defined exception class'''

	def __init__(self, length, atleast):

		Exception.__init__(self)
		self.length = length
		self.atleast =atleast

try:

	text = input("Enter text : ")
	atleast = 8

	if len(text) < atleast:
		raise ShortInputException(len(text),atleast)

except ShortInputException as ex:
	print('''ShortInputException: The input was 
		{} long , expected at least {}'''.format(ex.length,ex.atleast))
else:
	print("No Exception !!")


