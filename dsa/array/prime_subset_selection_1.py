class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        sum_primes = 0
        primes_arr = []
        for elem in range(2, n + 1):
            if self.is_prime(elem):
                sum_primes += elem
                if sum_primes > s:
                    break
                primes_arr.append(elem)
        return primes_arr


    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


n = 7
s = 20
sol = Solution()
result = sol.maxPrimes(n, s)
print(result)