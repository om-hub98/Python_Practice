input_arr = [1,2,3,1,3,4,5,4,5]

def find_unique_element(arr):
    non_unique_elements = set()
    unique_element = None
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                non_unique_elements.add(arr[i])
                break
    for element in arr:
        if element not in non_unique_elements:
            unique_element = element
            break
    return unique_element


print(find_unique_element(input_arr))


# optimized solution
print("Optimized solution:")
def find_unique_element_optimized(arr):
    unique_element = 0
    for element in arr:
        unique_element ^= element
    return unique_element

print(find_unique_element_optimized(input_arr))


