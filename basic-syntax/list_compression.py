nums = [1, 2, 3, 4, 5]

print("Traditional way - to iterate and store values :")
# Syntax 1 - traditional way
def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result

print(square_numbers(nums))  # Output: [1, 4, 9, 16, 25]

# Syntax 2 - list comprehension
print("\nList comprehension example:")
def square_numbers_list(nums):
    return [num * num for num in nums if num%2 == 0]

squared_list = square_numbers_list(nums)
print(squared_list)  # Output: [4, 16]