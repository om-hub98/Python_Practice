## TWO SUM PROBELM ::::
# Inputs :: 
numbers = [3,2,4]
target = 6
# Get index of a number in a list :: Time complexity is O(n^2) because of nested loop
result = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] + numbers[j] == target):
            result.append(i)
            result.append(j)
else:
    print(f"{target} is not in the list.")

print(f"Indices of {target} in the list: {result}")


# TIME cOMPLEXITY O(n)
seen = {}
for index, num in enumerate(numbers):
    complement = target - num
    if complement in seen:
        print(f"Indices of {target} in the list: [{seen[complement]}, {index}]")
        break  
    seen[num] = index