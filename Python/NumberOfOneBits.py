class Solution:
    def countBits(self, n):
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

def main():
    n = 11111111111111111111111111111101
    s = Solution()
    print(s.countBits(n))

if __name__ == "__main__":
    main()
