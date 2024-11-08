# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input('Enter name: ')
# TODO: Ask the user for their age and store it in a variable
age = input('Enter age: ')
# TODO: Print a greeting using the name and age variables
print('Greetings!' + ' ' + name + ' ' + age)
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input('Enter a length of a rectangle: '))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input('Enter a width of a rectangle: '))
# TODO: Calculate the area of the rectangle
area = (length * width)
# TODO: Print the result
print(str(area) + ' '+ 'is the area of the rectangle!')
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
Celsius = float(input('Enter a temperature in °C: '))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Temp = (Celsius * 9/5) + 32
# TODO: Print the result rounded to two decimal places
print(str(Temp) + 'F')