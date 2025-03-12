# Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1, no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:

	Value = 0   # class variable

	def __init__(self,no1,no2):
		self.no1 = no1
		self.no2 = no2

	def Fun(self):
		print("\nInstace variable for Fun method \n")
		print("No1 : ",self.no1)
		Obj1.Value = 1
		Obj2.Value = 2
		print("Class variable for obj1 : ",Obj1.Value)
		print("Class variable for obj2 : ",Obj2.Value)


	def Gun(self):
		print("\nInstace variable for Gun method \n")
		print("No2 : ",self.no2)
		Obj1.Value = 3
		Obj2.Value = 4
		print("Class variable for obj1 : ",Obj1.Value)
		print("Class variable for obj2 : ",Obj2.Value)


if __name__ == '__main__':

	Obj1 = Demo(int(input("Enter value for Obj1 no1 : ")),int(input("Enter value for Obj1 no2 : ")))
	Obj2 = Demo(int(input("Enter value for Obj2 no1 : ")),int(input("Enter value for Obj2 no2 : ")))

	Obj1.Fun()
	Obj2.Fun()

	Obj1.Gun()
	Obj2.Gun()

