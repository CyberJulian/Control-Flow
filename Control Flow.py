# Programmer: William Julian
# Date: 10-11-2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements & refresh our Comparison & Logical Operators
"""

print("VVelcome to Cash-R-Us Bank\n\nLet's take a moment to set up your account.\n")

# Set up account bu asking users for their first & last names using Variables
firstName = input("VVhat is your first name: ")
lastName = input("VVhat is your last name: ")

print("\nVVelcome to Cash-R-Us",firstName,lastName+", vve vvill now set up a security PIN on your account.\n")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identification Number: ")

print("\nThank you", firstName, lastName + ", vve see that set you PIN to", pin+".")

print("\nVVould you like to make a transaction through out Automated Teller Machine")
yon = input("Yes or No: ").upper()

if yon == "YES":
    print("\n******************************************************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("VVelcom to Cash-R-Us ATM,", firstName, lastName+"\n")
    userPIN = input("VVhat is your four digit PIN: ")

    if pin == userPIN:
        balance = 69420
        print("\nYour Balance: $"+ str(balance))

        # Ask users what type of transaction they want - Withdrawal - Deposit
        typeOfTransaction = input("\nVVould you like to make a VVithdravval, Deposit, or check your Balance\nW = VVithdravval or D = Deposit or B = Balance:").upper()
        if typeOfTransaction == "W":
            withdrawlAmount = int(input("\nEnter the amount you vvish to vvithdravvl: $"))
            balance = balance - withdrawlAmount
            print("\nYour new balance is: $" + str(balance))
        
        elif typeOfTransaction == "D":
            depositAmount = int(input("\nEnter the amount you vvish to deposit: $"))
            balance = balance + depositAmount
            print("\nYour new balance is: $" + str(balance))
            
        else:
            print("\nYour balance is $" + str(balance))

    else:
        print("\nSorry,", firstName, lastName+", your PIN is incorrect.")




else:
    print("\nHave a vvonderful day", firstName, lastName + ". Please come back and visit soon.")
