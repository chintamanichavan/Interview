def findTheDifference(s, t):
    diff = 0
    for char in s:
        diff ^= ord(char)
    for char in t:
        diff ^= ord(char)
    return chr(diff)

# Test the function with the given examples
print(findTheDifference("abcd", "abcde"))  # Expected output: "e"
print(findTheDifference("", "y"))  # Expected output: "y"
