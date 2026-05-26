input = "My name is Omraj Pradhan"
output = "Pradhan Omraj is name My"

def reverse_word(s:str)->str:
    words = s.split()
    left , right = 0, len(words)-1
    while left < right:
        temp = words[left]
        words[left] = words[right]
        words[right] = temp
        left += 1
        right -= 1
    return ' '.join(words)

print(reverse_word(input))