def reverse_string(input:str)-> str:
    """
    Reverses the given input string.
    Using for loop to iterate through the string in reverse order and build the reversed string.

    Args:
        input (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """

    result = ""
    for i in range(len(input),0,-1):
        result += input[i-1]
    return result


def reverse_string_slicing(input:str)-> str:
    """
    Reverses the given input string using slicing technique.
    [start:stop:step] - Here, we are using step as -1 to reverse the string.

    Args:
        input (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input[::-1]   # take the whole string and step backwards by 1 

'''
: for start/stop = use the whole sequence
: again before -1 means default end
-1 is the step
'''

def main():
    input_str = "Hello, World!"
    #reversed_str = reverse_string(input_str)
    reversed_str = reverse_string_slicing(input_str)
    print(f"Original String: {input_str}")
    print(f"Reversed String: {reversed_str}")
    

if __name__ == "__main__":
    main()
