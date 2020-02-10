# Write a Python class to convert an integer to a roman numeral.

class Converter:

	int_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

	roman_syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


	def int_to_roman(self,num):
		roman_num = ""

		if num in Converter.int_val:
			x = Converter.int_val.index(num)
			roman_num = Converter.roman_syb[x]

		else:
			i = 0
			while num > 0:
				for n in range(num // Converter.int_val[i]):
					roman_num += Converter.roman_syb[i]
					num -= Converter.int_val[i]
				i += 1
	 	
		return roman_num


if __name__=='__main__':
	converter = Converter()

	print(converter.int_to_roman(int(input("Enter a number : "))))




