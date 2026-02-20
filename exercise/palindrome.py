# Check if the input string is a palindrome

def _main():
    while(True):
        word = input("Enter a word to check palindrome or not \n")
        print("Palindrome" if isPalindrome(word) == True else "Not Palindrome")

        print("Do you want to continue? (y/n)")
        choice = input()
        if(choice.lower() != 'y'):
            break
        if(choice.lower() == 'y'):
            continue

def isPalindrome(word):
    word = word.lower()
    left = 0
    right = len(word)-1
    while(left <= right):
        if(word[left] != word[right]):
            return False
        left += 1
        right -= 1
    return True
    
_main()