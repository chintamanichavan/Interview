from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Column-wise DFS from least-significant digit. For each column, assign digits
        # to unbound letters of each word; once all word letters in the column are bound,
        # compute the column sum, derive the required digit for result[col], propagate carry.
        if max(len(w) for w in words) > len(result):
            return False

        rev_words = [w[::-1] for w in words]
        rev_result = result[::-1]
        leading = {w[0] for w in words + [result] if len(w) > 1}

        char_to_digit: dict[str, int] = {}
        used = [False] * 10

        def dfs(col: int, idx: int, carry: int) -> bool:
            if col == len(rev_result):
                return carry == 0
            if idx < len(rev_words):
                w = rev_words[idx]
                if col >= len(w) or w[col] in char_to_digit:
                    return dfs(col, idx + 1, carry)
                ch = w[col]
                for d in range(10):
                    if used[d] or (d == 0 and ch in leading):
                        continue
                    char_to_digit[ch] = d
                    used[d] = True
                    if dfs(col, idx + 1, carry):
                        return True
                    del char_to_digit[ch]
                    used[d] = False
                return False

            col_sum = carry + sum(char_to_digit[w[col]] for w in rev_words if col < len(w))
            digit = col_sum % 10
            next_carry = col_sum // 10
            r_ch = rev_result[col]
            if r_ch in char_to_digit:
                if char_to_digit[r_ch] != digit:
                    return False
                return dfs(col + 1, 0, next_carry)
            if used[digit] or (digit == 0 and r_ch in leading):
                return False
            char_to_digit[r_ch] = digit
            used[digit] = True
            if dfs(col + 1, 0, next_carry):
                return True
            del char_to_digit[r_ch]
            used[digit] = False
            return False

        return dfs(0, 0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.isSolvable(["SEND", "MORE"], "MONEY"))           # True
    print(s.isSolvable(["SIX", "SEVEN", "SEVEN"], "TWENTY")) # True
    print(s.isSolvable(["LEET", "CODE"], "POINT"))           # False
    print(s.isSolvable(["A", "B"], "C"))                     # True (e.g. 1 + 2 = 3)
    print(s.isSolvable(["ACA"], "JA"))                       # False (3-digit cannot equal 2-digit)
