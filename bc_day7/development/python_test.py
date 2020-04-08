# Comparison is a way to test items agains each other


a = 5
b = 22
c = 21
d = c
# Nesting is method to show which statement belong to what function
# indented block

# if (a > b){
# 	print('A is less than B', a)

# print('This statement does not have any indentation')

# if(True):
# 	print('This statement HAS indentation')

# # Less Than
# if (a < b):
# 	print('A is Greater than B')
# # Greater than
# elif (c > b):
# 	print('C is Greater than B')

# # Greater than or Equal to
# elif (b >= a):
# 	print('B is Greater than A')

# # If all other cases Fail
# else:
# 	print('All others Failed')

# Inequality
# if (d != a):
# 	print('D is not equal A')
# else:
# 	print('D is equal A')



# if (a < b) and (c < b):
# 	print('this is an example of multiple options')



# if (a > b) or (c > b):
# 	print('if both statements are True this is Printed')


# True and True = True
# True and False = False
# False and False = False


# True or True = True
# True or False = True
# False or False = False

# string_one = 'This is a String'
# string_two = 'this is a string'

# if (string_one == string_two):
# 	print('both Strings are equal')
# elif (string_one.lower() == string_two.lower()):
# 	print('both lowercase strings are equal')
# else:
# 	print('neither is equal')



# IN Operator can test whether items are in the list or not
# my_list = [12,45,34,56,123,12,3,2,4]
# num = 12


# if num in my_list:
# 	print(num)

while True:
	import random

	options = ['rock', 'paper', 'scissors']
	choice = input('Enter your Choice: ')
	choice = choice.lower()
	computer = random.choice(options)

	print(f'You chose {choice} and the computer chose {computer}')

	if (choice == 'rock') and (computer == 'paper'):
		print('Computer Wins')
	elif (choice == 'rock') and (computer == 'scissors'):
		print('You Wins')
	elif (choice == 'scissors') and (computer == 'rock'):
		print('Computer Wins')
	elif (choice == 'scissors') and (computer == 'paper'):
		print('You Wins')
	elif (choice == 'paper') and (computer == 'scissors'):
		print('Computer Wins')
	elif (choice == 'paper') and (computer == 'rock'):
		print('You Wins')
	else:
		print("It's a tie!!")





# For Loops do something for each value
# ForEach loop 

items = [12,45,34,56,123,12,3,2,4]

# Enumerate
# for item in items:
# 	# Don't have a way to increment without index number
	

# for item in items:
# 	if(item >= 21):
# 		print(f'You are {item} years old, You can enter')
# 	else:
# 		print(f'You are only {item} years old and cannot enter')


# Print Index
# for index, item in enumerate(items):
# 	print(index, item)

# print('After the For Loop is done', index, item)

# List Comprehension - Python Specific Feature
# result = [[index, item] for index, item in enumerate(items)]
# print(result)
# print('After the For Loop is done', index, item)

# Generators / List Comprehension
# people_over_21 = [age for age in items if age >= 21]
# print(people_over_21)
# for item in people_over_21:
# 	print(item)


# While - Repeat until a parameter is met

# i = 10
# counter = 0
# while counter <= 10:
# 	print("Only run for a little bit", counter)
	
# 	# Break Case for Loop
# 	counter += 1
# print('While loop is finised!!!!')


# If / Elif / Else / For Loop / While Loop

# Conditional run 1 Time
# If / elif / else Run only 1 Time

# Loops Run until the Break Case
# For Break Case (python For is really forEach)
# - For loops run until the end of the list/dictionary

# While Loops - Will repeat until a break case is met

# Conditional can be put inside a loop












































