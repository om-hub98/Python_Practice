class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        num1, num2 = 0, 1
        while (num1 + num2) <= n:
            next_fib = num1 + num2
            reqd_next = n - (num1 + num2)
            if next_fib == reqd_next:
                return True
            num1, num2 = num2, next_fib
        return False


n = 2
sol = Solution()
result = sol.threeFibonacciSum(n)
print(result)