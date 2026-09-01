test_cases = {4:[1,4,4], 7:[2,3,1,2,4,3], 11:[1,1,1,1,1,1,1]}


# Naive approach
# Time complexity: O(n^2)
# Failes for large input arrays
def min_subarray_len(target: int, nums:list[int]) -> int:
    min_len = float('inf')
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum >= target:
                min_len = min(min_len, j - i + 1)
                break
    return 0 if min_len == float('inf') else min_len

# Optimized Array
def min_subarray_len_optimized(target: int, nums: list[int]) -> int:
    min_len = float("inf")
    left = 0
    right = 0
    sum = 0
    while right < len(nums):
        sum += nums[right]
        while sum >= target:
            min_len = min(min_len, right - left + 1)
            sum -= nums[left]
            left += 1
        right += 1
    return 0 if min_len == float("inf") else min_len


def execute_main():
    n = 1
    for key, value in test_cases.items():
        print(f"Test Case number {n} ---> Target : {key} - Input Array : {value} ---> Minimum Length of Subarray : {min_subarray_len_optimized(key, value)}")
        n += 1

if __name__ == "__main__":
    execute_main()
