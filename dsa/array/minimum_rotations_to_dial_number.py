class Solution:
    def minRotations(self, s: str) -> int:
        total_distance = 10
        current_digit = 0
        sum = 0
        for n in s:
            distance = abs(int(n) - current_digit)
            shortest_distnce = min(distance, total_distance - distance)
            sum += shortest_distnce
            current_digit = int(n)
        return sum


sol = Solution()
print(sol.minRotations("0192837465")) 


            