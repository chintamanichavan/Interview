
def findRotateSteps(ring: str, key: str) -> int:
    from collections import defaultdict
    import sys

    # Map each character in the ring to all indices where it appears
    char_to_indices = defaultdict(list)
    for i, ch in enumerate(ring):
        char_to_indices[ch].append(i)

    n = len(ring)
    m = len(key)

    # DP array, where dp[i][j] means the minimum steps to spell up to key[i] and stop at ring[j]
    dp = [[sys.maxsize] * n for _ in range(m)]

    # Initialize the DP table for the first character in the key
    for index in char_to_indices[key[0]]:
        # Minimum of clockwise or anticlockwise steps from initial position 0
        dp[0][index] = min(index, n - index) + 1  # +1 for pressing the button

    # Fill the DP table for each subsequent character in the key
    for i in range(1, m):
        for curr_index in char_to_indices[key[i]]:
            for prev_index in char_to_indices[key[i-1]]:
                # Calculate distance clockwise and anticlockwise
                clockwise_steps = abs(curr_index - prev_index)
                anticlockwise_steps = n - clockwise_steps
                # Update the DP value considering all possible previous positions
                dp[i][curr_index] = min(dp[i][curr_index], dp[i-1][prev_index] + min(clockwise_steps, anticlockwise_steps) + 1)

    # The answer is the minimum value in the last row of dp table
    return min(dp[-1])

# Example usage
ring = "godding"
key = "gd"
print(findRotateSteps(ring, key))  # Output: 4
