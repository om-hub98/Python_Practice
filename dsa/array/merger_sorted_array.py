nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

#nums1 = [0]
#nums2 = [1]

def merger_sorted_array(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    
    if m == 0:
        for i in range(n):
            nums1[k] = nums2[i]
            k -= 1

    while i>=0 and j>=0:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        else:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
    return nums1
print(merger_sorted_array(nums1, 3, nums2, 3))