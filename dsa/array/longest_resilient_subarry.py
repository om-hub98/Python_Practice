class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        max_length = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                sum_subarray = sum(subarray)
                is_resilient = True
                for num in subarray:
                    rem = sum_subarray - num
                    if rem % k != 0:
                        is_resilient = False
                        break
                if is_resilient:
                    max_length = max(max_length, len(subarray))
        return max_length

nums = [2,4,6,3]
k = 2
sol = Solution()
result = sol.resilientSubarray(nums, k)
print(result)