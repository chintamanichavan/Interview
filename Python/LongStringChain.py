def longestStrChain(words):
    # Sort the words based on their length
    words.sort(key=len)
    
    # Dictionary to store the maximum chain length for each word
    chain_lengths = {}
    max_chain = 1

    for word in words:
        chain_lengths[word] = 1
        # Generate all possible words by removing one character
        for i in range(len(word)):
            prev_word = word[:i] + word[i+1:]
            # If the generated word exists in the dictionary, update the maximum chain length for the current word
            if prev_word in chain_lengths:
                chain_lengths[word] = max(chain_lengths[word], chain_lengths[prev_word] + 1)
                max_chain = max(max_chain, chain_lengths[word])

    return max_chain

# Test the function with the given examples
print(longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Expected output: 4
print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Expected output: 5
print(longestStrChain(["abcd","dbqca"]))  # Expected output: 1
