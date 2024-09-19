import heapq
class Solution():
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = list(zip(profits, capital))
        heapq.heapify(projects)

        for _ in range(k):
            while projects and projects[0][1] <= w:
                profit = heapq.heappop(projects)[0]
                w += profit

            if not projects:
                break

        return w

def main():
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    s = Solution()
    res = s.findMaximizedCapital(k, w, profits, capital)
    print(res)

if __name__ == '__main__':
    main()
