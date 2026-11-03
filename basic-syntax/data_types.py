  ### Data Types in Python ####

#print("1"+2) # This will raise an error because you cannot concatenate a string and an integer directly.
str_concat = "1"+"2"
print(str_concat) # This will print "12" because both operands are strings.
print(type(str_concat)) # This will print <class 'str'> because the result is a string.

int_concat = 1+2
print(int_concat) # This will print 3 because both operands are integers.
print(type(int_concat)) # This will print <class 'int'> because the result is an integer.

# Integers & Floats 
integer_num = 10
decimal_num = 3.12

#String
string_var = "Hello, World!"

# List
list_var = [1, 2, 3, 4]
tuple_var = (1, 2, 3)

# dictionary
dict_var = {'id': 101, 'name': 'Omraj', 'age': 26}

# boolean
bool_var = True

# Data Manipulation

print("Integer : ", integer_num)
print("Float : ", decimal_num)
print("String : ", string_var + " Welcome to Python!")
list_var.append(5)
print("List : ", list_var)
print("Tuple : ", tuple_var)
print("Dictionary : ", dict_var['name'])
print("Boolean : ", bool_var)