# """
# GLOBAL SCOPE
# """

# """
# Variable
# """

# my_num = 5 #IMMUTABLE 
# my_string = '5' #IMMUTABLE
# my_tuple = (5) # IMMUATABLE LIST
# my_list = [5, 6, 7] #MUTABLE
# my_dict = {'key1': 5, 'key2': 6, 'key3': 7} #MUTABLE


# """
# Conditionals
# """
# # def if_test():
# # 	if (my_num == my_string):
# # 		print('Number and Strings are Equal')
# # 	elif (my_num != my_string):
# # 		print('Number and Strings are NOT Equal')
# # 	else:
# # 		print('Neither was True')

# # if_test()

# # print(type(my_num))
# # print(type(my_string))



# # """
# # For loop
# # """
# # def for_test():
# # 	for item in my_list:
# # 		if(my_num == item):
# # 			print(item)

# # for_test()
# # def enumerate_test():
# # 	for index, item in enumerate(my_list):
# # 		print(index, item)

# # # print('after for loop is done: ', index, item)

# # def for_dict():
# # 	for key, value in my_dict.items():
# # 		print(key, value)

# # for_dict()
# # # # List Comprehension - Pythonistic programming

# # def list_comp():
# # 	result = [[i,it] for i, it in enumerate(my_list)]
# # 	print(result)

# # list_comp()
# # # print('after list comprehension is done: ', i, it)
# # def while_test():
# # 	start = 0
# # 	end = 10
# # 	while start < end:
# # 		# print('This will never stop', start, end)
# # 		print(f'The current count is at {start} and will end at {end}')
# # 		start += 1 # start = start + 1

# # print(while_test())


# # Functions Expect a Return Deliverable
# # def function():
# # 	if(True or False):
# # 		print(True)
# # 		return True
# # 		print('Print This')

# # print(function())


# """
# SCOPE LOCAL vs GLOBAL
# """

# # x = 'This is a Global Variable'

# # def x_test():
# # 	# First will look inside the function for variable
# # 	# Then look outside function
# # 	global x #Can do this but SHOULD NOT!!!
# # 	x = 'This is a local Variable'
# # 	return x

# # print(x_test())
# # print(x)

# """
# Extra Arguments - Args
# """

# # def add_func(num1, num2, num3):
# # 	print('First position is ',num1)
# # 	print('Second positon is ',num2)
# # 	print('Third positon is ',num3)
# # 	return num1 + num2 + num3

# # print(add_func([7,5,8], [9,10], [11,12]))


# # def extra_arguments(placeholder1, placeholder2, placeholder_everything_else)
# # def extra_arguments(asdf, num2, *args):
# # 	# print('asdf', asdf)
# # 	# print('num2', num2)
# # 	print('*args', args)
# # 	print(type(args))
# # 	# args = 'something else'
# # 	return asdf, num2, args

# # print(extra_arguments([1,2,3],'string', 'extra_arguments', 'another', 50, 100))

# """
# KeyWord Arguments
# """

# # def kw_args(ph1, ph2, *args, **kwargs):
# # 	print('placeholder1', ph1)
# # 	print('placeholder2', ph2)
# # 	print('*args', args)
# # 	print('**kwargs', kwargs)
# # 	return ph1, ph2, args, kwargs

# # print(kw_args([1,2], [3,4], 'extra_arguments', 50, 100, another_arg='another_arg', another='another'))

	
# """
# Decorators
# """

# import datetime

# def decorator(func):
# 	def wrapper():
# 		# print('before decoration')
# 		# start_time = datetime.datetime.today()
# 		# Output time funtion ran, what function, who called it
# 		if (Check if user is authenticated - then run)

# 			func()
# 		else:
# 			send to login screen
# 		# print('after decoration')
# 		# end_time = datetime.datetime.today()
# 		# Output end time of function execution, what function who called, cID, function ID,
# 		print(end_time - start_time)
# 	return wrapper

# @decorator
# def i_need_decorator_func_one():
# 	print('func One')
# 	out = []
# 	for i in range(5000):
# 		out.append(i)
# 	return out

# @decorator
# def i_need_decorator_func_two():
# 	print('func Two')
# 	return [i for i in range(5000)]

# # i_need_decorator_func_one = decorator(i_need_decorator_func_one)
# i_need_decorator_func_one()

# # i_need_decorator_func_two = decorator(i_need_decorator_func_two)
# i_need_decorator_func_two()

# # # i_need_decorator()
# # i_need_decorator = decorator(i_need_decorator)
# # print(i_need_decorator())


# # When to use a decorator
# Logging each time we run a function






# Celsius = float(input())
celsius = float(input('Enter degrees Celsius that you want to conver to Fahrenheit: '))

# No need to initialize this value
# Fahrenheit = float() 

# def convert(Celsius):
def convert(cel):
  return (((cel) * 9) / 5) + 32

# print("Celsius: " + str(Celsius) + " Fahrenheit: " + str(convert(Celsius)))

# We can use print formatting to make the output easier to read
# """ make it Multi-Line
# %.2f makes floats only have 2 decimal places
print(f"""Celsius: {celsius}
Fahrenheit: {'%.2f' % convert(celsius)}""")







