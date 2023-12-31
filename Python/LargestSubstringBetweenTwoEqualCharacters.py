class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Array to store first and last positions of each character
        positions = [[-1, -1] for _ in range(26)]
        
        for i, char in enumerate(s):
            char_index = ord(char) - ord('a')
            if positions[char_index][0] == -1:
                positions[char_index][0] = i
            positions[char_index][1] = i

        # Calculate the maximum length of substring
        max_length = -1
        for first, last in positions:
            if first != -1 and last != -1:
                max_length = max(max_length, last - first - 1)

        return max_length
