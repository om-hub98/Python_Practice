def fact(n):
    #base condition
    if n==0:
        return 1
    else:
        return n*fact(n-1) 
    
print("The factorial of 5 is:", fact(5))