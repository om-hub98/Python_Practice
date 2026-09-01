input_word = "the sky is blue"

def reverse_words_in_string(s: str) -> str:
    s_arr = s.split()
    left, right = 0, len(s_arr) - 1
    while left < right:
        s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
        left +=1
        right -=1
    return " ".join(s_arr)


print(reverse_words_in_string(input_word))
