# EY interview Question
# Move all zeros to the right

input = [0,1,2,4,0,3,5]

# Solution 1 => Simple using extra space
# Approach - 1. Create a new list to store non_zeros.
#          - 2. Count the number of zeros in the input list.
#          - 3. Append the counted number of zeros to the new list.

def process_zeros(input: list[int]):
    temp_input = []
    for elem in input:
        if elem != 0:
            temp_input.append(elem)
    zeros_needed = len(input) - len(temp_input)
    while zeros_needed > 0:
        temp_input.append(0)
        zeros_needed = zeros_needed - 1
    
    return temp_input
    
    
# Optimized code => in-place
# Approach - 1.Move all non_zeros to left and keep track of the index of the last non_zero element.
#          - 2. Fill the remaining elements of the list with zeros.
def process_zeros_optimized(input: list[int]):
    track_index = 0
    for index in range(len(input)):
        if input[index] != 0:
            input[track_index] = input[index]
            track_index += 1
            
    while track_index < len(input):
        input.append(0)
        track_index += 1
        
    return input

    
print(process_zeros(input))