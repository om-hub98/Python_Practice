def lengthOfLastWord(input: str) -> int:
    words = input.strip().split()
    if not words:
        return 0
    return len(words[-1])


def main():
    while True: 
        user_input = input("Enter a string: ")
        print(lengthOfLastWord(user_input))

        print("Do you want to continue? (y/n): ")
        continue_input = input().lower()
        if continue_input != 'y':
            break 
    print("Goodbye!")


if __name__ == "__main__":
    main()