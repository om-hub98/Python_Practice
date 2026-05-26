input = "Omraj_Pradhan"

def remove_underscore_from_string(input_str):
    for ch in input_str:
        if ch == '_':
            input_str = input_str.replace('_', ' ')
    return input_str


print(remove_underscore_from_string(input))


# optimized code
def remove_underscore_from_string_optimized(input_str):
    return input_str.replace('_', ' ')

print(remove_underscore_from_string_optimized(input))