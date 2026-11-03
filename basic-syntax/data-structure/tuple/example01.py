my_tuple = ('Omraj', 25, 'Engineer', 'India', 3.8)
print("Original Tuple:", my_tuple)
# Accessing elements
print("Name:", my_tuple[0])

print(isinstance(my_tuple, tuple))  # True
print(type(my_tuple))  # <class 'tuple'>

# Modifying tuple
# Tuples are immutable, so we cannot modify them directly. However, we can create a new tuple.
print("Modifying Tuple:")
my_tuple[0] = 'John'  # This will raise an error since tuples are immutable
print("Modified Tuple:", my_tuple)
