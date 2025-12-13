fruits_list = ["apple", "banana", "cherry"]
for item in fruits_list:
    print(item)

# split string by space and print string
print("==== Splitting string by space and printing each word: ====")
sample_str = "This is a sample string"
str_list = sample_str.split(" ")
for word in str_list:
    print(word)


# print last word length from the list
print("==== Length of last word in the list: ====")
words = ["hello", "world", "python", "programming"]
last_word = words[-1]
print(len(last_word))


#sprint and print ;ast string length
print("==== Length of last word in the sentence: ====")
sentence =" I am a boy "
print("Original length:", len(sentence))
trim_words = sentence.strip()
print(len(trim_words))
split_words = trim_words.split(" ")
last_word = split_words[-1]
print(len(last_word))