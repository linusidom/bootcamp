# STRING INDEXING
# my_string = 'django'
# print(my_string[1]) # d
# print(my_string[-1]) # o
# print(my_string[0:4]) # djan
# print(my_string[1:4]) # djan
# print(my_string[-2:]) # go
# print(my_string[::-1])

# LIST CHANGING
# my_list = [3,'hello',[1,4,'change_me']]
# print(my_list) # [3, 'hello', [1, 4, 'change_me']]
# my_list[2][2] = 'changed'
# print(my_list) # [3, 'hello', [1, 4, 'changed']]

# DICTIONARY INDEXING
# d1 = {'k1':'print_me'}
# d2 = {'k1':{'k2':'print_me'}}
# d3 = {'k1':[{'nested_key':['37',['print_me']]}]}
# print(d1['k1']) # print_me
# print(d2['k1']['k2']) # print_me
# print(d3['k1'][0]['nested_key'][1][0]) # print_me
# print(d1)
# d1['k1'] = "Don't print me"
# print(d1)


# ADDING TUPLES
# my_tuple = (1, 2, 3)
# my_tuple = my_tuple + (5,6,7)
# print(my_tuple)

# first_name = 'Changed'
# last_name='Name'

# print(f'Welcome to the DjanoPy BootCamp {first_name} {last_name}') #'Welcome to the DjanoPy BootCamp John Doe'

# I want to add 2 numbers together

import unittest

def sumNum(arg1,arg2):
	return arg1 + arg2

# Given a list of integers, return True if the sequence of numbers 1, 2, 3 is in the list
def arrayCheck(arr):
	for i in range(len(arr) - 2):
		if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
			return True
	return False

# Given a string, return a new string made of every other character
def stringBits(ph1):
	# print(ph1[::2])
	return ph1[::2]


# Given two strings, return True if either of the strings appears at the very end
def end_other(string1, string2):
	if string1.lower() in string2.lower() or string2.lower() in string1.lower():
		return True
	return False

# Given a string, return a string where for every char in the original there are 2 character
def doubleChar(string1):
	# result = []
	# for i in string1:
	# 	result.append(i*2)
	# return ''.join(result)
	# List Comprehension
	return ''.join([i*2 for i in string1])

def fix_teen(num):
	nums = [13,14,17,18,19]
	if num in nums:
		return 0
	return num

def no_teen_sum(a,b,c):
	return fix_teen(a) + fix_teen(b) + fix_teen(c)

# Return the number of even integers in the given array.
def count_evens(arr):
	# result = []
	# for i in arr:
	# 	if i % 2 == 0:
	# 		result.append(i)
	# return len(result)
	
	# count = 0
	# for i in arr:
	# 	if i % 2 == 0:
	# 		count += 1
	# return count

	return len([i for i in arr if i % 2 == 0])
	
# Test is of type unittest.TestCase
class TheseAreOurTestCases(unittest.TestCase):
	def test_sumNumbers(self):
		self.assertEqual(sumNum(3,3), 6)
		self.assertEqual(sumNum(3,2), 5)
	def test_willFail(self):
		self.assertEqual(False, False)
	def test_arrayCheck(self):
		self.assertEqual(arrayCheck([1, 1, 2, 3, 1]),True)
		self.assertEqual(arrayCheck([1, 1, 2, 4, 1]),False)
		self.assertEqual(arrayCheck([1, 1, 2, 1, 2, 3]),True)
	def test_stringBits(self):
		self.assertEqual(stringBits('Hello'),'Hlo')
		self.assertEqual(stringBits('Hi'),'H')
		self.assertEqual(stringBits('Heeololeo'),'Hello')
	def test_end_other(self):
		self.assertEqual(end_other('Hiabc', 'abc'),True)
		self.assertEqual(end_other('AbC', 'HiaBc'),True)
		self.assertEqual(end_other('abc', 'abXabc'),True)
		self.assertEqual(end_other('abc', 'def'),False)
	def test_doubleChar(self):
		self.assertEqual(doubleChar('The'),'TThhee')
		self.assertEqual(doubleChar('AAbb'),'AAAAbbbb')
		self.assertEqual(doubleChar('Hi-There'),'HHii--TThheerree')
	def test_no_teen_sum(self):
		self.assertEqual(no_teen_sum(1, 2, 3),6)
		self.assertEqual(no_teen_sum(2, 13, 1),3)
		self.assertEqual(no_teen_sum(2, 1, 14),3)
		self.assertEqual(no_teen_sum(2, 1, 15),18)
	def test_count_evens(self):
		self.assertEqual(count_evens([2, 1, 2, 3, 4]),3)
		self.assertEqual(count_evens([2, 2, 0]),3)
		self.assertEqual(count_evens([1, 3, 5]),0)

# print(dir(TestCases))

unittest.main()













