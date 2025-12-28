# Set in python
# it holds only only unique elements

elements = {1,2,3}
elements.add(2)  # Duplicate element, will not be added
print(elements)  # Output: {1, 2, 3}

elements.add(4)
print(elements)  # Output: {1, 2, 3, 4}  

elements.remove(3)
print(elements)  # Output: {1, 2, 4}

#union, intersection in sets

sets1 = {1,2,3}
sets2 = {3,4,5}

print(sets1 | sets2) # Output: {1, 2, 3, 4, 5}   note : duplicate 3 is removed
print(sets1 & sets2) # Output: {3}  # common element
print(sets1 - sets2) # Output: {1, 2}  # elements in sets1 but not in sets2
