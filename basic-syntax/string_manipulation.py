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



#5. Indexing and slicing

## please note => 
## Single colon =>      start:stop =>      1:4=> means start index : stop index (exclude stop index)
## Double colon mean => start:stop:step    ::3 => means start index is 0: stop index length of string : step (every 3rd character) 
text = "Python"
print("First character : ", text[0])  # Output: P
print("Last character : ", text[-1])  # Output: n
print("Substring : ", text[1:4])  # Output: yth
print("Every second character : ", text[::2])  # Output: Pto
print("Reversed string : ", text[::-1])  # Output: nohtyP
print("Characters third last to end : ", text[-3:])  # Output: hon
# text[0] = "J"  # This will raise an error because strings are immutable in Python
# print("Modified text : ", text)  # Output: TypeError: 'str' object does not support item assignment



