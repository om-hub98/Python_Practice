'''
def greet(name):
    return f"Hello, {name}!"

print(greet("Omraj"))
'''


# **kwargs => Keyword Arguments - used when you don't know number of keyword argument
#Example 1
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Omraj", age=25, city="Kolkata")

#Example 2
def display_info(**info):
    return f"Name: {info['name']}, Age: {info['age']}, City: {info['city']}"

print(display_info(name="Pradhan", age=50, city="Delhi"))