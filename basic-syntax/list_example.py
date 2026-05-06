numbers = [1, 2, 3, 4, 5]
append_numbers = []
for num in numbers:
    append_numbers.append(num)

print("Appended numbers : ", append_numbers)  # Output: ['1,', '2,', '3,', '4,', '5,']


## Flat nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []
for outer in nested_list:
    for inner in outer:
        flattened_list.append(inner)

print("Flattened list : ", flattened_list)  # Output: [1, 2, 3, 4, 5, 6]


## Flatted  deeply nested loop

flattened_deeply_nested_list = []
def flatten_list(nested):
    for item in nested:
        if isinstance(item, list):
            flatten_list(item)  # Recursive call for nested lists
        else:
            flattened_deeply_nested_list.append(item)
            

deeply_nested_list = [1, [2, [3, [4, [5]]]]]
flatten_list(deeply_nested_list)

print("Flattened deeply nested list : ", flattened_deeply_nested_list)  # Output