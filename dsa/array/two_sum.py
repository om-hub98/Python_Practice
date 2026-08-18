
input_arr = [2, 7, 11, 15]
#input_arr = [-1,0]

def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]


def two_sum_optimized(numbers: list[int], target: int) -> list[int]:
    num_dict = {}
    for index, elem in enumerate(numbers):
        diff = target - elem
        if diff in num_dict:
            return [num_dict[diff] + 1, index + 1]
        num_dict[elem] = index


# Without using any extra space
# Two Pointer approach  - where left and right pointers are used for traversing array
def two_sum_optimized_2(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1

#print(two_sum(input_arr, -1))
#print(two_sum_optimized(input_arr, -1))
print(two_sum_optimized_2(input_arr, 9))

