def factorials(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorials(num - 1)
    

def print_factorials(n):
    for i in range(n+1):
        print(f"Factorial of {i} is {factorials(i)}")

print_factorials(5)