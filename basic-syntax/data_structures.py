## Data Structures in python

# List, tuples, sets, dictionaries


print("List Example")
### List in python
# ordered collectio
# mutable, allows duplicate elements

numbers = [1, 2, 3, 4, 5]  # List
print(numbers[-2])  # Output: 4 # Accessing elements using negative indexing

fruits = ["apple", "banana", "cherry"]  # List of strings
print(fruits[2])  # Output: ['apple', 'banana', 'cherry']

mixed = [1, "hello", 3.14, True]  # List with mixed data types
print(mixed[0])  # Output: [1, 'hello', 3.14, True]


fruits.append("orange")  # Adding an element to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape")  # Inserting an element at a specific index
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

sliced_fruits = fruits[1:4]  # Slicing the list 1 - start index, 4 - end index (exclusive)
print(sliced_fruits)  # Output: ['grape', 'banana', 'cherry']




print("Tuples Example")
## Tuples in python
# ordered collection
# immutable, allows duplicate elements

colors = ("red", "green", "blue")  # Tuple
print(colors[1])  # Output: green

# colors.append("yellow")  # This will raise an error since tuples are immutable
# print(colors)  # Output: ('red', 'green', 'blue')



## Dictionary in python
# unordered collection of key-value pairs
# mutable, keys must be unique
print("Dictionary Example")

person= {"name": "John", "age": 30, "city": "Kolkata"}
print(person["name"])  # Output: John


# Iteration of dictionary 
for key, value in person.items():
    print(f"{key}: {value}")



## Sets in python
# unordered collection of unique elements
print("Set Example")

set1 = {1,2,3}
set2 = {3,4,5}
set1.add(2)  # Duplicate element, will not be added
print(set1)  # Output: {1, 2, 3}
print(set1 | set2)    # union of set1 and set2  # Output: {1, 2, 3, 4, 5}   note : duplicate 3 is removed
print(set1 & set2)    # intersection of set1 and set2  # Output: {3}  # common element
print(set1 - set2)    # difference of set1 and set2  # Output

