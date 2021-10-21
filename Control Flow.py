# Programmer: William Julian
# Date: 10-11-2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements & refresh our Comparison & Logical Operators
"""

print("VVelcome to Cash-R-Us Bank\n\nLet's take a moment to set up your account.\n")

# Set up account bu asking users for their first & last names using Variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nVVelcome to Cash-R-Us",firstName,lastName+", we will now set up a security PIN on your account.\n")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identification Number: ")

print("\nThank you", firstName, lastName + ", we see that set you PIN to", pin+".")


print("\nWould you like to make a transaction through out Automated Teller Machine")