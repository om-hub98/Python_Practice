class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        result = []
        max_product = float('-inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and nums[i] != nums[j] and nums[i] > nums[j]:
                    product = nums[i] * nums[j]
                    if product > max_product:
                        max_product = product
                        result = [i, j]
        return result


nums = [1,2,3,4]
target = 5
sol = Solution()
result = sol.maxProductPair(nums, target)
print(result)