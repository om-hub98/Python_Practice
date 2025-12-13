# This is a simple Python program to print "Hello, World!" to the console.

# Step 1: Use the print() function
# The print() function is a built-in Python function that outputs text to the console.
# Here, we pass the string "Hello, World!" as an argument to the print() function.
print("Hello, World!")

my_name = "Omraj Pradhan"
print("My name is", len(my_name))

#What will be the output of below code snippets?
print("*" * 10)

# Substring in python
print(my_name[0:])   #prints entire string -  Omraj Pradhan
print(my_name[0:9])   # print till index-1 - Omraj Pra
print(my_name[:])     # prints entire string - Omraj Pradhan
print(my_name[:9])    # print till index-1 - Omraj Pra
print(my_name[0])     # prints first character - O
print(my_name[-1])     # prints last character - n

# Escape sequences in python  
# e.g:  \n(new line), \t(tab), \'(apostrope), \"(double quote), \\(slash)
print("Hello,\nWorld!")  # prints Hello, World! in new line
print("Hello,\"World!")  # prints Hello, "World! in new line

## Formatted Strings in Python
# Formatted strings (f-strings) allow you to embed expressions inside string literals, using curly braces {}.
first_name = "Omraj"
last_name = "Pradhan"
print(f"{len(first_name)} {last_name}")  # Output: Omraj Pradhan
#print({first_name} + " " + {last_name})  # Output: Omraj Pradhan

# default functions in python
full_name = "Omraj Pradhan"
print(full_name.upper())    # prints the string in uppercase - OMRaj PRADHAN
print(full_name.lower())    # prints the string in lowercase - omraj pradhan
print(full_name.title())    # prints the string in title case - Omraj Pradhan
print(full_name.rsplit())    # prints the string as a list - ['Omraj', 'Pradhan']
print(full_name.replace("Omraj", "Om"))  # replaces Omraj with Om - Om 
print(full_name.find("Pradhan"))  # finds the index of Pradhan - 6
print("Pra" in full_name)
print("Omiw" in full_name)


## Mathematical expression
a = 10
b = 5.3
comples_nuber = 3 + 5j
print(3 + 5)    # Addition - 8
print(10 - 2)   # Subtraction - 8       
print(4 * 2)    # Multiplication - 8
print(16 / 3)   # Division - 8.0
print(17 // 2)  # Floor Division - 8
print(3 ** 2)   # Exponentiation - 9
print(17 % 3)   # Modulus - 2   
print(round(3.6))  # Rounds the number to nearest integer - 4

## data types in python
#int(x)
#float(x)
#bool(x)
#str(x)

print(int(5.7))    # converts float to int - 5
print(float(5))    # converts int to float - 5.0

#input from terminal in python
name = input("Enter your name: ")
print(f"Hello, {name}!")

###Falsy values in Python
# In Python, the following values are considered "falsy," meaning they evaluate to False in
# a boolean context:
# 1. None
# 2. False
# 3. Zero of any numeric type: 0
# 4. Empty sequences and collections: '', (), [], {}
print(bool(0))          # Output: False
print(bool(""))         # Output: False     
print(bool([]))         # Output: False
print(bool({}))         # Output: False
print(bool(None))       # Output: False
print(bool(False))      # Output: False     
print(bool(42))         # Output: True
print(bool("False"))    # Output: True