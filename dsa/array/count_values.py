class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        nums_dict = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = []
            nums_dict[nums[i]].append(i)

        for key, values in nums_dict.items():
            #print(f"Value: {key}, Indices: {len(values)}")
            if len(values) >= 3:
                diff = values[1] - values[0]
                is_special = True
                for i in range(1, len(values)):
                    if values[i] - values[i-1] != diff:
                        is_special = False
                        break
                if is_special:
                    count += 1
        return count

sol = Solution()
print(sol.countSpecialIntegers([8,8,8,8]))

                
        
        
        
        