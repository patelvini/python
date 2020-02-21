# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1, Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(),
# Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1, Value2 and return
# result.
# Subtraction() method will perform subtraction of Value1, Value2 and
# return result.
# Multiplication() method will perform multiplication of Value1, Value2 and
# return result.
# Division() method will perform division of Value1, Value2 and return
# result.
# After designing the above class call all instance methods by creating
# multiple objects.

class Arithmetic:

	def __init__(self):
		self.Value1 = 0.0
		self.Value2 = 0.0
		self.result = 0.0

	def Accept(self,Value1,Value2):
		self.Value1 = Value1
		self.Value2 = Value2
		
	def Addition(self):
		self.result = self.Value1 + self.Value2
		return self.result

	def Subtraction(self):
		self.result = self.Value1 - self.Value2
		return self.result
		

	def Multiplication(self):
		self.result = self.Value1 * self.Value2
		return self.result

	def Division(self):
		self.result = self.Value1 / self.Value2
		return self.result

if __name__ == '__main__':

	obj1 = Arithmetic()
	obj2 = Arithmetic()
	
	print("For obj1 : \n")
	obj1.Accept(int(input("Enter Value 1 : ")),int(input("Enter Value2 : ")))
	print("Addition = ",obj1.Addition())
	print("Subtraction = ",obj1.Subtraction())
	print("Multiplication = ",obj1.Multiplication())
	print("Division = ",obj1.Division())
	

	print("\n For obj2 : \n")
	obj2.Accept(int(input("Enter Value 1 : ")),int(input("Enter Value2 : ")))
	print("Addition = ",obj2.Addition())
	print("Subtraction = ",obj2.Subtraction())
	print("Multiplication = ",obj2.Multiplication())
	print("Division = ",obj2.Division())
	
	