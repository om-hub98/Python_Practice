class Solution:
    def plusOne(self, nums: list[int]) -> list[int]:
        for index in range(len(nums)-1, -1, -1):
            print(f"{index}: {nums[index]}")
            if nums[index] < 9:
                print(f"nums[index] < 9: {nums[index]}")
                nums[index] += 1
                print(nums)
                return nums
            nums[index] = 0
        return [1] + nums


sol = Solution()
nums = [1,2,3]
print(sol.plusOne([9]))

print([100] + nums)
nums1 = [0] * len(nums)
print(nums1)