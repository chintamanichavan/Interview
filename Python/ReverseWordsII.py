def reverseWords(s):
    # Split the string into words
    words = s.split()
    
    # Reverse each word and join them back together
    return ' '.join(word[::-1] for word in words)

# Test the function with the given examples
print(reverseWords("Let's take LeetCode contest"))  # Expected output: "s'teL ekat edoCteeL tsetnoc"
print(reverseWords("God Ding"))                    # Expected output: "doG gniD"
