# def initialization(name, age, height, weight):
# 	return {'name':name,'age':age,'height':height,'weight':weight}

# def get_age(person):
# 	return f"{person['name']} is {person['age']} years old"

# def get_height(person):
# 	return f"{person['name']} is {person['height']} cm tall"

# def get_weight(person):
# 	return f"{person['name']} is {person['weight']} kilos"


# DRY - Don't Repeat Yourself



# If we want to Track more than 1 Variable/Attribute, we should try to use Classes

# Classes

class Person(object):

	# Attributes - Same as Variables but Attributes are inside of a class
	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	# Method - Same as Function but Methods are inside of a Class 
	def __str__(self):
		# John is 35 years old and is 175 cm tall and weight approx 80 kilos
		return f"{self.name.title()} is {self.age} years old and is {self.height} cm tall and weighs approx {self.weight} kilos"

	def get_age(self):
		return f"{self.name} is {self.age} years old"

	def get_height(self):
		return f"{self.name} is {self.height} cm tall"

	def get_weight(self):
		return f"{person['name']} is {person['weight']} kilos"


class Employee(Person):
		# Attributes - Same as Variables but Attributes are inside of a class
	def __init__(self, name, age, height, weight, wage):
		super().__init__(name, age, height, weight)
		# self.name = name
		# self.age = age
		# self.height = height
		# self.weight = weight
		self.wage = wage

	# Method - Same as Function but Methods are inside of a Class 
	def __str__(self):
		# John is 35 years old and is 175 cm tall and weight approx 80 kilos
		return f"{self.name.title()} is {self.age} years old and is {self.height} cm tall and weighs approx {self.weight} kilos"

	def get_wage(self):
		return f"{self.name} is paid {self.wage} baht per month"

