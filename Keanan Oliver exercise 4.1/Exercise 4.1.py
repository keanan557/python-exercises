#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students, absentees):
    return absentees
# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees , and print the result.
print(check_attendance( ["Alice", "Bob", "Charlie", "David"] ,["Bob", "David"]))
#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(disctionary,values):
# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
    def operation_selector(add, multiply):
        return function(add,multiply)
# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
        operation_selector(4,6)
# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.

#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    fuel_needed = distance/fuel_efficiency
    total_cost = fuel_needed * fuel_price
    return total_cost
# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.
for item in grocery_inventory:
    print(grocery_inventory)
# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).


#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
pin= input('enter pin: ')
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
correct_pin = "1234"
attempts = 0
max_attempts= 3
while attempts < max_attempts:
    pin = input('enter pin: ')
    if pin == correct_pin:
        print('Welcome!')
        break
    else:
        attempts +=1
        print('wrong, try again')

    if attempts == max_attempts:
        print('Account locked')

# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".



# TODO: Use a while loop to implement the retry system.


#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.


#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)
import random
# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.



# List of participants.
participants = ["Person1", "Person2", "Person3", ..., "Person20"]

# TODO: Randomly select 5 people from the participants list.


#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
from fitness_tracker import walk_calories, run_calories, cycle_calories
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
user_input = int(input('Enter your distance walked: '))
# TODO: Calculate and print the total calories burned for each activity.

# TODO: Sum and print the total calories burned for the day.


#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
total_loan_amount = float(input('Enter total loan amount: '))
# TODO: Ask the user to input their monthly repayment amount.
monthly_repayment = float(input('Enter monthly amount: '))
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
while True:
    total_loan_amount= total_loan_amount - monthly_repayment
# TODO: Print the remaining loan amount after each payment.
print(total_loan_amount)
# TODO: When the loan is fully paid off, print a congratulatory message.

loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.

