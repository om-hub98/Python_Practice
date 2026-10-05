nums = [1, 2, 3, 4, 5, 6]
print("Example to demonstrate Using generator:")
# Syntax 1 - Generator function - traditional way
# yield - used to return the value from the function and it will return a generator object
def square_numbers(nums):
    for num in nums:
        yield num * num

squared_nums = square_numbers(nums)
print(next(squared_nums))  # Output: 1
print(next(squared_nums))  # Output: 4
print(next(squared_nums))  # Output: 9
        
#Syntax 2 - Generator function shorthand -> generator expression
def shorthand_squre_numbers(nums:list[int]):
    return (num * num for num in nums if num%2 == 0)

print("\nPrint even squared numbers:")
#even_squared_nums = (num * num for num in nums if num%2 == 0)    # Genertor expression -> RETURNs generator objects
even_squared_nums = shorthand_squre_numbers(nums)
print(next(even_squared_nums))  # Output: 4
print(next(even_squared_nums))  # Output: 16
print(next(even_squared_nums))  # Output: 36


# Real Scenario - Use case -> Streaming LLM response
def stream_llm_response():
    response_chunks = [
        "The ",
        "customer ",
        "has ",
        "3 ",
        "orders."
    ]

    for chunk in response_chunks:
        yield chunk

print("\nStreaming LLM response:")
llm_response = stream_llm_response()
for _ in range(5):
    print(next(llm_response))  # Output: The





