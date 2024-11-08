# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ['apple', 'peach', 'cherry']
# TODO: Add a fruit to the end of the list
fruits.append('grapes')
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, 'guava')
# TODO: Remove a fruit from the list
fruits.remove('apple')
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]
# TODO: Create a new list with each number squared
numbers_squared = [1,2**2,3**2,4**2,5**2]
# TODO: Find the sum and average of the original numbers
s = sum(numbers)
average = s/len(numbers)
# TODO: Print the results
print(s)
print(average)
print(numbers_squared)
print(numbers)
#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
dict = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "South Africa": "Pretoria"  # Note: South Africa has three capitals
}
# TODO: Add a new country-capital pair
dict['Mexico'] = 'Mexico City'
# TODO: Update the capital of an existing country
dict["Australia"] = "Sydney"
# TODO: Remove a country-capital pair
dict.pop('India')
# TODO: Print the modified dictionary
print(dict)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    'orange' : 'orange',
    'grape' : 'purple',
    'apple' : 'red',
    'banna' : 'yellow'
}
# TODO: Print all the fruits (keys)
print(fruit_colors.keys())
# TODO: Print all the colors (values)
print(fruit_colors.values())
# TODO: Print each fruit and its color
print(fruit_colors)
# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = 'orange'
if fruit_to_check in fruit_colors:
    print(f'color of {fruit_to_check} is {fruit_colors[fruit_to_check]}')
else:
    print('not in dictionary')