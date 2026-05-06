#print stars in one directional
# iteraton is i++
for i in range(1, 6):
    print("Index :", i, "*" * i)

print("Iteration in +2 steps")

#print i+2
for i in range(1, 10, 2):
    print("Index :", i, "*" * i)

print("Reverse the iteration")
#print in reverse
for i in range(5, 0, -1):
    print("Index :", i, "*" * i)


# for else use case
print("For else use case")
success = True
for i in range(1, 6):
    print("Attempted")
    if success:
        print("Success!")
        break
else:
  print("Failed after 5 attempts")

# nested for loop
print("Nested for loop")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")


# string iteration
print("String iteration")
str = "Hello"
for ch in str:
    print(ch)

# iterating over a list
print("Iterating over a list")  
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)

# while loop
print("While loop example")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# iterating over a dictionary
print("Iterating over a dictionary")
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")   


# infinite loop with break
'''
print("Infinite loop with break")
while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")
'''
# print even numbers from 1 to 20
print("Even numbers from 1 to 20")
count = 1
for num in range(1, 20):
    if num%2==0:
        print(num)
        count+=1
print("Total even numbers:", count)



# Check letter in string
fruit = "apple"
if "a" in fruit:
    print("Letter 'a' is present in the fruit name.")
else:  
    print("Letter 'a' is not present in the fruit name.")



