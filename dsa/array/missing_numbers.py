nums = [1,5]

def find_missing_numbers(nums):
    n = len(nums)
    nums.sort()
    expected_arr = []
    for i in range(n-1):
        next_num = nums[i] + 1
        while nums[i+1] != next_num:
            expected_arr.append(next_num)
            next_num += 1
    
    missing_numbers = []
    for elem in expected_arr:
        if elem in nums:
            continue
        missing_numbers.append(elem)
    return missing_numbers


def find_missing_numbers_optimized(nums):
    n_max = max(nums)
    n_min = min(nums)
    missing_numbers = [n for n in range(n_min, n_max) if n not in nums]
    return missing_numbers


#print(find_missing_numbers(nums))
print(find_missing_numbers_optimized(nums))