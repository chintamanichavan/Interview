def minDeletionsToMakeGood(s):
    # Create a dictionary to count character frequencies
    char_count = {}
    
    # Count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Create a set to store unique frequencies
    unique_freq = set()
    
    # Initialize the total deletions count
    deletions = 0
    
    for freq in char_count.values():
        # While the current frequency is already in unique_freq, increment it and count the deletion
        while freq in unique_freq:
            freq -= 1
            deletions += 1
        
        # Add the adjusted frequency to unique_freq
        if freq > 0:
            unique_freq.add(freq)
    
    return deletions

# Example usage:
s1 = "aab"
print(minDeletionsToMakeGood(s1))  # Output: 0

s2 = "aaabbbcc"
print(minDeletionsToMakeGood(s2))  # Output: 2

s3 = "ceabaacb"
print(minDeletionsToMakeGood(s3))  # Output: 2
