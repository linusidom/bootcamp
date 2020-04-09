# Celsius = float(input())
celsius = float(input('Enter degrees Celsius that you want to conver to Fahrenheit: '))

# No need to initialize this value
# Fahrenheit = float() 

# def convert(Celsius):
def convert(cel):
	# Fahrenheit = ((Celsius * 9) / 5) + 32
	# return Fahrenheit

	# Can return the whole function in one line
	return (((cel) * 9) / 5) + 32

# print("Celsius: " + str(Celsius) + " Fahrenheit: " + str(convert(Celsius)))

# We can use print formatting to make the output easier to read
# """ make it Multi-Line
# %.2f makes floats only have 2 decimal places
print(f"""Celsius: {celsius}
Fahrenheit: {'%.2f' % convert(celsius)}""")