import heapq
from math import prod

nums = [-4, -1, 0, 4, 5, 10]

def maximum_product_of_three_numbers(nums):
    nums.sort()
    n = len(nums)
    prod1 = nums[n-1] * nums[n-2] * nums[n-3]
    prod2 = nums[0] * nums[1] * nums[n-1]

    return max(prod1, prod2)


def maximum_product_of_three_numbers_optimized(nums):
    largest = heapq.nlargest(3, nums)
    print(largest)
    smallest = heapq.nsmallest(2, nums)
    print(smallest)
    return max(prod(largest), prod(smallest) * largest[0])

#print(maximum_product_of_three_numbers(nums))
print(maximum_product_of_three_numbers_optimized(nums))