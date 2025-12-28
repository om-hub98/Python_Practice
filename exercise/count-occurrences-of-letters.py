
# Pthyon script to count occurrences of each letter in a given string

def count_occurrences_of_letters(input_string):
    dict_of_letter_count = {}       # Intialize empty dictionary to store letter counts
    for char in input_string:
        if char in dict_of_letter_count:
            dict_of_letter_count[char] += 1
        else:
            dict_of_letter_count[char] = 1

    return dict_of_letter_count


def count_occurrences_of_words(input_string):
    dict_of_word_count = {}       # Intialize empty dictionary to store word counts
    words = input_string.split()  # Split the string into words based on whitespace
    for word in words:
        if word in dict_of_word_count:
            dict_of_word_count[word] += 1
        else:
            dict_of_word_count[word] = 1

    return dict_of_word_count


user_input = input("Enter a string to count letter occurrences: ")
print(count_occurrences_of_letters(user_input))

user_input = input("Enter a string to count word occurrences: ")
print(count_occurrences_of_words(user_input))