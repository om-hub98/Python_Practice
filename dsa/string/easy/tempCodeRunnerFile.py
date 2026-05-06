def lengthOfLastWord(input: str) -> int:
    words = input.strip().split()
    if not words:
        return 0
    return len(words[-1])