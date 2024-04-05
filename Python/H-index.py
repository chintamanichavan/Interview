class Solution():
    def hIndex(self, citations):
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations
        for c in citations:
            papers[min(n, c)] += 1  # For citations larger than n, we count them as n
        k = n
        s = papers[n]  # s is the number of papers with more than k citations
        while k > s:
            k -= 1
            s += papers[k]
        return k


def main():
    citations = [3,0,6,1,5]
    s = Solution()
    res = s.hIndex(citations)
    print(res)

if __name__ == '__main__':
    main()
