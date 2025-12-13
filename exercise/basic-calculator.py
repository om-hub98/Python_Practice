
## Basic Calculator for addition, Subtraction, Multiplication, and Division.
## Application should continue as long as user wants to perform calculations

def add(num1,num2) :
    return num1 + num2

def subtract(num1,num2) :
    return num1 - num2  

def multiply(num1,num2) :
    return num1 * num2

def divide(num1,num2) :
    return num1 / num2


while True:
    print("## Basic Calculator ##")
    print("#Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == '5':
        print("Exiting the program.")
        break
    
    elif choice in ['1','2','3','4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(f"Sum of {num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"Subtraction of {num1} - {num2} = {subtract(num1,num2)}")
        elif choice == '3':
            print(f"Multiplication of {num1} * {num2} = {multiply(num1,num2)}")
        elif choice == '4':
            if num2 != 0:
                print(f"Division of {num1} / {num2} = {divide(num1,num2)}")
            else:
                print("Error: Division by zero is not allowed.")    
    else:
        print("Invalid choice. Please select a valid option.")