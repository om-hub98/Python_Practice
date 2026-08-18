# Find longest Substring Without Repeating Characters
input_s = "abcabcbabc"

# Naive Approach
# Time Complexity: O(n^2)
def longest_substring(s:str) -> int:
    max_length =0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                max_length = max(max_length, len(seen))
            seen.add(s[j])
        
    return max_length


def longest_substring_optimized(s:str) -> int:
    seen = set()
    left  = 0 
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


#print(longest_substring(input_s))
print(longest_substring_optimized(input_s))