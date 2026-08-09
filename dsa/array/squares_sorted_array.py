nums = [-7,-3,2,3,11]

#nums = [-5,-3,-2,-1]

def squares_sorted_array(nums):
    left = 0
    right = len(nums) - 1
    pos = len(nums) - 1
    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left]**2)
            pos -= 1
            left += 1
        else:
            result.append(nums[right]**2)
            pos -= 1
            right -= 1

    index = 0
    for i in range(len(result)-1, -1, -1):
        nums[index] = result[i]
        index += 1
    return nums

print(squares_sorted_array(nums))

