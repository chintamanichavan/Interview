def winnerOfGame(colors: str) -> bool:
    count_A = count_B = 0
    n = len(colors)
    
    # Count segments of continuous 'A's
    i = 0
    while i < n:
        if colors[i] == 'A':
            start = i
            while i < n and colors[i] == 'A':
                i += 1
            if i - start > 2:
                count_A += i - start - 2
        i += 1
    
    # Count segments of continuous 'B's
    i = 0
    while i < n:
        if colors[i] == 'B':
            start = i
            while i < n and colors[i] == 'B':
                i += 1
            if i - start > 2:
                count_B += i - start - 2
        i += 1
        
    return count_A > count_B

# Test the function with the given examples
print(winnerOfGame("AAABABB"))        # Expected output: true
print(winnerOfGame("AA"))             # Expected output: false
print(winnerOfGame("ABBBBBBBAAA"))    # Expected output: false
