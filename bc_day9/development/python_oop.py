john_name = 'john'
john_age = 35
john_height = 175
john_weight = 80

jane_name = 'jane'
jane_age = 40
jane_height = 150
jane_weight = 40

print('Variables Only')
print(john_name, john_age, john_height, john_weight)
print(jane_name, jane_age, jane_height, jane_weight)

john_list = ['john', 35, 175, 80]
jane_list = ['jane', 40, 150, 40]

print('Lists')
print(john_list)
print(jane_list)

john_dict = {
	'name': 'john',
	'age': 35,
	'height': 175,
	'weight': 80
}

jane_dict = {
	'name': 'jane',
	'age': 40,
	'height': 150,
	'weight': 40
}
print('Dictionaries')
print(john_dict)
print(jane_dict)
# What if we had to create Bob and Laura using the same method?

from python_file import get_age, get_height, initialization, get_weight

def initialization(name, age, height, weight):
	return {'name':name,'age':age,'height':height,'weight':weight}

def get_age(person):
	return f"{person['name']} is {person['age']} years old"

def get_height(person):
	return f"{person['name']} is {person['height']} cm tall"


john = initialization('john', 35, 175, 80)
jane = initialization('jane', 40, 150, 40)
bob = initialization('bob', 55, 180, 90)
laura = initialization('laura', 40, 170, 65)

print('Functions')
print(john)
print(jane)
print(bob)
print(laura)

print('Get Age')
print(get_age(john))
print(get_age(jane))
print(get_age(bob))
print(get_age(laura))

print('Get Height')
print(get_height(john))
print(get_height(jane))
print(get_height(bob))
print(get_height(laura))

from python_file import Person, Employee
class Person:
	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	def get_age(self):
		return f"{self.name} is {self.age} years old"

	def get_height(self):
		return f"{self.name} is {self.height} cm tall"


john = Person('john', 35, 175, 80)
jane = Person('jane', 40, 150, 40)
bob = Person('bob', 55, 180, 90)
laura = Person('laura', 40, 170, 65)

print('Classes')
print(john.get_age())
print(jane.get_age())
print(bob.get_age())
print(laura.get_age())

print(dir(john))
print(help(john))


john = Employee('john', 35, 175, 80, 50000)
jane = Employee('jane', 40, 150, 40, 40000)
bob = Employee('bob', 55, 180, 90, 30000)
laura = Employee('laura', 40, 170, 65, 20000)

print('Class Inheritance')
print(john.get_age())
print(jane.get_age())
print(bob.get_age())
print(laura.get_age())

print(john.get_wage())
print(jane.get_wage())
print(bob.get_wage())
print(laura.get_wage())
print(dir(john))
print(help(john))

john = Employee('john', 35, 175, 80, 50000)
alex = Person('alex', 35, 175, 80)

print('John', type(john))
print('Alex' ,type(alex))

print('John',john.get_wage())
print('John',john.get_age())
print('John',john.get_height())

print(alex.get_wage())

















