class Solution:
    # Failed for test case : nums = [1,7] , k = 1
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        start, end = 0, len(nums)
        result = float('inf') 
        min_index = -1
        for index in range(len(nums)):
            max_num = max(nums[start:index+1])
            min_num = min(nums[index:end])
            diff = max_num - min_num
            if diff <= k:
                result = min(result, diff)
                min_index = index

        return min_index if min_index != -1 else -1


    # Prefix max and suffix min approach
    def firstStableIndex_optimized(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_so_far = nums[0]
        suffix_min = nums[-1]
        suffx_min_list = []
        for element in nums:
            max_so_far = max(max_so_far, element)
        for i in range(n-1, -1, -1):
            suffix_min = min(suffix_min, nums[i])
            suffx_min_list.append(suffix_min)

        suffx_min_list.reverse()
        for i in range(n):
            if max_so_far - suffx_min_list[i] <= k:
                return i

        return -1

sol = Solution()
print(sol.firstStableIndex_optimized([5,0,1,4], 3))
print(sol.firstStableIndex_optimized([1,7], 1))
        