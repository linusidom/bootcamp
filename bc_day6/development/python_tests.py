"""
Numbers Review
"""

# Integer - 5, 10, 40
# Float - 5.0, 10.123124, 100.00

# Math with Numbers
# PEMDAS
# ()
# **
# *
# (/,//,%)
# +
# -

# String
# string = 'string'
# print(string[3])

# string_one = 'This is'
# string_two = ' a string'

# print(string_one[0:5])
# print(string_one + string_two)

# john_age = 35
# john_hair_color = 'brown'

# print(john_age, john_hair_color)

"""
introduction Lists
"""

# john = [35, 'brown']
# print('John ', john)
# print(john)
# john[1] = 'black'
# print(john)

# Lists Are MUTABLE
# Lists are Ordered Comma Separated Values
# Because Lists are ordered they are slow!!!!!!


# Append is add values to the List

# john_height = 175
# john.append(john_height)
# print('john',john)

# jane = [40, 'blond']
# jane_height = 160
# jane.append(jane_height)
# print('Jane', jane)

# print(jane + john)

# Pop Remove Values from the List

# john.pop()
# print(john)

# john.pop(0)
# print(john)

# Delete The Entire List
# del john
# print(john)



# Insert Values into Array
# john.insert(1,175)
# print(john)


# Not a real copy but just assigment of Pointers from Memory
# bob = john

# print('Bob ',bob)

# bob[0] = 40

# print('Bob', bob)
# print('John', john)




# Real way to make copies
# This keeps Bob Separate from any Changes that occur with John

# bob = []

# for item in john:
# 	bob.append(item)

# print('Bob ',bob)

# bob[0] = 40

# print('Bob', bob)
# print('John', john)

# Error list index out of range
# print(john[2])

# Length or Size of the List
# print(len(john))

# my_list = ['a','b','c','a','d','a']

# print('How many times does A show up? ',my_list.count('a'))


# We have John in a single list, with no columns

"""
dictionaries
"""

# Dictionaries are Unordered (changed in Python 3)
# MUTABLE, can change values inside the dictionary
# (Key : Value) Pair
# (Word : Definition of the word)


# john = [35, 'brown']
# jane = [40, 'blonde']

# noSQL Entry - this is okay - CAN store JSON object directly
my_dict = {
	'tf-ready-stock-i264214907-s1752282609': {
		'title': 'TF New fashion Coin Purses Coin Purse Oil skin Clutch Retro Coin bag Card package',
		'price': 15,
		'ratings': 7,
	},
	'jane': {
		'age': 40,
		'hair_color': 'blonde'
	},
}

# SQL entry - This is NOT Okay!!! - CANNOT store JSON object directly
# my_dict = {
# 	'tf-ready-stock-i264214907-s1752282609': {
# 		'title': 'TF New fashion Coin Purses Coin Purse Oil skin Clutch Retro Coin bag Card package',
# 		'price': 15,
# 		'ratings': 7,
# 	},
# 	'ab-ready-stock-i264214907-s1752282610': {
# 		'title': 'Must have Title',
# 		'price': 'Must have Price (no data okay, but have to have the same column)',
# 		'ratings': 'Must ratings',
# 	},
# }

# SQL Database
my_dict['id'] =  'tf-ready-stock-i264214907-s1752282609'
my_dict['tf-ready-stock-i264214907-s1752282609']['title'] = 'TF New fashion Coin Purses Coin Purse Oil skin Clutch Retro Coin bag Card package'




# print(my_dict)

# print(my_dict['tf-ready-stock-i264214907-s1752282609']['price'])

# Customer Fills out a Form
# Form Data will get stored in Database
# Webpage will pull Data from database as a Dictionary Object



my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for item in my_list:
	print('Unncessary but have to in Lists', item)
	if(item == 13):
		print('Found it!!', item)

print(my_dict['jane']['age'])

























































































