def decodeAtIndex(s, k):
    # Compute the length of the decoded string.
    length = 0
    for ch in s:
        if ch.isdigit():
            length *= int(ch)
        else:
            length += 1

    # Walk backward to find the k-th character.
    for ch in reversed(s):
        k %= length
        if k == 0 and ch.isalpha():
            return ch

        if ch.isdigit():
            length //= int(ch)
        else:
            length -= 1
