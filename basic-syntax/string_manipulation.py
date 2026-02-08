#  String manipulation functions

#1. Conatenation
first_name = "John"
last_name = "Doe"   
full_name = first_name + " " + last_name
print("Full Name : ", full_name)  # Output: John Doe

#2. Repetition
greeting = "Hello! "
repeated_greeting = greeting * 3
print("Repeated Greeting : ", repeated_greeting)  # Output: Hello! Hello! Hello

#3. Slicing
message = "Hello, World!"
print("Sliced Message : ", message[0:5])  #prints letters between start index 0 & end index 5 (excluding)  # Output: Hello
print("Sliced Message : ", message[7:])   #prints  everything starting from index 7    #Output: World!
print("Reverse message : ", message[::-1]) #prints the string in reverse order  # Output: !dlroW ,olleH


#4. Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String : ", formatted_string)  # Output: My name is Alice and I am 30 years old.
