nums = [-1,0,1,2,-1,-4]

def three_sum(nums : list) -> list:
    result = list()
    nums.sort()
    sum = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if sum==0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:
                        result.append(triplet)
    return result


def three_sum_optimied(nums:list) -> list:
    result = list()
    nums.sort()
    for x in range(0, len(nums) - 2):

        if x > 0 and nums[x] == nums[x - 1]:
            continue
        left = x + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[x] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[x], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                right -= 1
                left += 1
            elif sum > 0:
                right -= 1
            else:
                left += 1
    return result

#print(three_sum(nums))
print(three_sum_optimied(nums))