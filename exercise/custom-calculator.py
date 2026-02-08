   ## Basic Calculator for addition, Subtraction, Multiplication, and Division.
## Application should continue as long as user wants to perform calculations

import basic_calculator as calc

while True:
    print("\n## Basic Calculator ##")
    print("\nMenu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice : ")

    if(choice == '1'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Sum of {num1} + {num2} = {calc.sum(num1,num2)}")
    elif(choice == '2'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Subtraction of {num1} - {num2} = {calc.subtract(num1,num2)}")
    
    elif(choice == '3'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Multiplication of {num1} * {num2} = {calc.multiply(num1,num2)}")

    elif(choice == '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Division of {num1} / {num2} = {calc.divide(num1,num2)}")
    
    elif(choice == '5'):
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
