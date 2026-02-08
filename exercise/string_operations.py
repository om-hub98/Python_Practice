def get_substring(str, start, end):
    return str[start:end]

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):
    str = str[::-1]

def count_vowels(str):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))