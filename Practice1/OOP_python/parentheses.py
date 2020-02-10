class Parentheses:

	def valid_parentheses(self,str1):
		stack = []

		pchar = {'(':')','{':'}','[':']'}

		for p in str1:
			if p in pchar:
				stack.append(p)
			elif len(stack)==0 or pchar[stack.pop()] != p:
				return False
		return len(stack) == 0

if __name__ == '__main__':

	paren = Parentheses()

	print(paren.valid_parentheses(input("Enter a string with parentheses : ")))

