from collections import deque

class Solution():
    def letterCombinations(self, digits):
      if not digits: return []

      digitToChar = {
          "2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "pqrs",
          "8": "tuv",
          "9": "wxyz"
      }

      queue = deque([""])

      for d in digits:
        for _ in range(len(queue)):
          currStr = queue.popleft()
          for c in digitToChar[d]:
            queue.append(currStr + c)

      return list(queue)


def main():
    digits = "23"
    s = Solution()
    result = s.letterCombinations(digits)
    print(result)

if __name__ == '__main__':
    main()
