class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        left_arr = []
        right_arr = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                for element in right_arr:
                    if nums[left] < element:
                        left_arr.append(nums[left])
                        left += 1
                        break
                right_arr.append(nums[right])
                right -= 1
            else:
                left_arr.append(nums[left])
                right_arr.append(nums[right])
                right -= 1
                left += 1
        return len(left_arr) + 1

    def partitionDisjoint_optimized(self, nums: list[int]) -> int:
        n = len(nums)
        max_left = float('-inf')
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        for i, elem in enumerate(nums):
            max_left = max(max_left, elem)
            if max_left <= suffix_min[i + 1]:
                return i + 1
        return -1

sol = Solution()
print(sol.partitionDisjoint([5,0,3,8,6]))
print(sol.partitionDisjoint([1,1,1,0,6,12]))
print(sol.partitionDisjoint_optimized([5,0,3,8,6]))
print(sol.partitionDisjoint_optimized([1,1,1,0,6,12]))
