num = "22-08-2026"

def num_to_word(num: str):
    map_num_words = {"0":"zero", "1":"one", "2": "two", "8":"eight", "6":"six"}  
    print(map_num_words)
    result = ""
    for i in range(len(num)):
        print(f"{i} : {num[i]}")
        if num[i] is not "-":
            result += map_num_words.get(num[i])
        else:
            result += num[i]
    return result

print(num_to_word(num))
	   