input = {'a': 1, 'b': 2, 'c': 3}

def swap_dict_key_value(input_dict):
    swapped_dict = {}
    for key, value in input_dict.items():
        swapped_dict[value] = key
    return swapped_dict


print(swap_dict_key_value(input))