# Create a Pets class that holds instances of dogs; 
# this class is completely separate from the Dog class. 
# In other words, the Dog class does not inherit from the Pets class. 
# Then assign three dog instances to an instance of the Pets class. 
# Start with the following code below. Save the file as pets_class.py. 

# Your output should look like this:
# I have 3 dogs. 
# Tom is 6. 
# Fletcher is 7. 
# Larry is 9. 
# And they're all mammals, of course.


class Pets:

	dogs = []

	def __init__(self,dogs):
		self.dogs = dogs


# Parent class
class Dog:

	#class attribute
	species = 'mammal'

	#Initializer
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.is_hungry = True

	# instance method
	def description(self):
		return "{} is {} years old".format(self.name,self.age)

	# instance method
	def speak(self,sound):
		return "{} says {}".format(self.name,sound)

	# instance method
	def eat(self):
		self.is_hungry = False


# Child class
class RussellTerrier(Dog):

	def run(self,speed):
		return "{} runs {}".format(self.name,speed)

# Child class
class Bulldog(Dog):

	def run(self,speed):
		return "{} runs {}".format(self.name,speed)


if __name__ == '__main__':

	# CREATE INSTANCE OF DOGS

	my_dogs = [Bulldog("Tom",6),RussellTerrier("Fletcher",7),Dog("Larry",9)]

	my_pets = Pets(my_dogs)

	print("I have {} dogs".format(len(my_pets.dogs)))

	for dog in my_pets.dogs:
		print("{} is {}.".format(dog.name,dog.age))

	print("And they're all {}s, of course.".format(do))