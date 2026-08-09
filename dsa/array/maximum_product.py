input_arr = 124

def maximum_product_of_two_digits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = n//10
    print(digits)
    max : int = 0
    for i in range(len(digits)):
        for j in range(i+1,len(digits)):
            prod = digits[i] * digits[j] 
            if prod > max:
                max = prod
    return max

print(maximum_product_of_two_digits(input_arr))


#Optimized Solution
def maximum_product_of_two_digits_optimized(n):
    d1, d2 = 0, 0
    while n > 0:
        d=n%10
        if d > d1:
            d2 = d1
            d1 = d
        elif d > d2:
            d2 = d
        n = n//10
    return d1*d2

print("Optimized solution:")
print(maximum_product_of_two_digits_optimized(input_arr))