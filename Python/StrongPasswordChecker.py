class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_type = 3
        if any(c.islower() for c in password):
            missing_type -= 1
        if any(c.isupper() for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1

        # Scan runs of >= 3 equal chars. Each run of length L needs L // 3 replacements.
        # Track how many runs have L % 3 == 0 (savable with 1 delete) and == 1 (with 2 deletes);
        # L % 3 == 2 runs need 3 deletes to save one replacement.
        change = 0
        one = two = 0
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(6 - n, missing_type)
        if n <= 20:
            return max(change, missing_type)

        # n > 20: deletions are mandatory; spend them to cut replacements in priority order.
        delete = n - 20
        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) // 2
        change -= max(delete - one - two * 2, 0) // 3
        return delete + max(change, missing_type)


if __name__ == '__main__':
    s = Solution()
    print(s.strongPasswordChecker("a"))         # 5
    print(s.strongPasswordChecker("aA1"))       # 3
    print(s.strongPasswordChecker("1337C0d3"))  # 0
    print(s.strongPasswordChecker("aaa123"))    # 1
    print(s.strongPasswordChecker("aaaaa"))     # 2
    print(s.strongPasswordChecker("1111111111"))# 3
    print(s.strongPasswordChecker("aaaabbaaabbaaabbaaabbaaaa"))  # n=25, deletions+runs
