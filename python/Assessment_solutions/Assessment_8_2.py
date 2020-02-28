# Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius, Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# There are three instance methods inside class as Accept(),CalculateArea(), CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
# And Display() method will display value of all the instance variables as Radius, Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:

	PI = 3.14

	def __init__(self):
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0

	def Accept(self,Radius):
		self.Radius = Radius

	def CalculateArea(self):
		self.Area = self.PI * (self.Radius**2)

	def CalculateCircumference(self):
		self.Circumference = 2 * self.PI * self.Radius

	def Display(self):
		print("Radius = ",self.Radius)
		print("Area = ",self.Area)
		print("Circumference = ",self.Circumference)

if __name__ == '__main__':

	circle1 = Circle()
	circle2 = Circle()
	
	print("For circle1 : \n")
	circle1.Accept(float(input("Enter radius for circle : ")))
	circle1.CalculateArea()
	circle1.CalculateCircumference()
	circle1.Display()

	print("\n For circle2 : \n")
	circle2.Accept(float(input("Enter radius for circle : ")))
	circle2.CalculateArea()
	circle2.CalculateCircumference()
	circle2.Display()

