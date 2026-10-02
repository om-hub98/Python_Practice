class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while len(nums) > 0:
            temp = []
            index = 0
            while index < len(nums):
                if nums[index] not in temp:
                    temp.append(nums[index])
                    nums.pop(index)  
                else:
                    index += 1
            temp.sort()
            ans.extend(temp)
        return ans

sol = Solution()
nums = [3,1,3,2,1,3]
print(sol.rearrangeArray(nums))
                