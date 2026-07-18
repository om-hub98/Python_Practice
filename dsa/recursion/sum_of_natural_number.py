def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

input = 3
print("The sum of first", input, "natural numbers is:", sum(input))