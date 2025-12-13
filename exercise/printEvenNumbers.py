# print even numbers from 1 to 20
print("Even numbers from 1 to 20")
num = 0
count  = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
        count+=1
    num += 1
print(f"We have {count} even numbers printed.")