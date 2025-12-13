### Comparison Operators
a = 10
b = 5
print(a > b)    # Greater than - True
print("omraj" < "Omraj")


### Conditional Operators
x = input("Enter a number: ")
x = int(x)
if x % 2 == 0:
    print("Even")
elif x == 0:
    print("Zero")
else:
    print("Odd")


## one line of code -> Ternary operator
x = int(input("Enter a number: "))
message = "Even" if x % 2 == 0 else "Odd"
print(message)


### Logical Operators
age = 18
high_school_passed = True
school_kid = True
if(age >= 18 and high_school_passed and not school_kid):
    print("Eligible for college admission")
elif(age < 18 or not high_school_passed):
    print("Not eligible for college admission")
else:
    print("Check other criteria")


