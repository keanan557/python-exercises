# # Question 1: Basic Function Definition and Calling

# # TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print('Hello, World')
# # TODO: Call the 'greet' function
greet()

# #------------------------------------------------------------------------------------
# # Question 2: Function with Parameters

# # TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
     print('Hi '+name)
# # TODO: Call the 'personalized_greeting' function with your name
personalized_greeting('Keanan')

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
def square(number2):
    square = number2**2
    return square
# TODO: Call the 'square' function with the number 5 and print the result
print(square(5))

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# # TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    area = length * width
    return area
# # TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(rectangle_area(4, 5))

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function, num):
    return function(num)


# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
   double = number*2
   return double

# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
#
print(apply_operation(double,7))
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
print(apply_operation(square,3))
