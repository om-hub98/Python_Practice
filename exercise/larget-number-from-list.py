
## Write Python script to find largest number form a list of numbers.

def largest_number_from_list(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest

def second_largest_number_from_list(numbers):
    if len(numbers) < 2 :
        return None
    
    first = max(numbers)
    second = float('-inf')  #Initialize second largest to negative infinity
   
    for num in numbers:
        if num > second and num != first:
            second = num
    return second

list_of_numbers_1 = [3, 45, 23, 67, 89, 2, 100, 34]
list_of_numbers_2 = [3, 3, 2]
list_of_numbers_3 = [10, 20]
print("Largest numbers from list : ",largest_number_from_list(list_of_numbers_1))
print("Second Largest numbers from list : ",second_largest_number_from_list(list_of_numbers_2))
print("Second Largest numbers from list : ",second_largest_number_from_list(list_of_numbers_3))

