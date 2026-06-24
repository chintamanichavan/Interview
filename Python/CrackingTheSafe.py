class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # The shortest sequence containing every length-n string over k digits as a substring is a
        # de Bruijn sequence. Build it with Hierholzer's algorithm: nodes are length-(n-1) prefixes,
        # edges are digits; an Euler circuit visits every length-n combination (edge) exactly once.
        if n == 1:
            return "".join(str(d) for d in range(k))

        seen = set()
        path = []

        def dfs(node: str) -> None:
            for d in range(k):
                edge = node + str(d)
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    path.append(str(d))

        start = "0" * (n - 1)
        dfs(start)
        return "".join(path) + start


if __name__ == "__main__":
    s = Solution()
    print(s.crackSafe(1, 2))  # 01
    print(s.crackSafe(2, 2))  # 01100
    print(s.crackSafe(3, 2))  # 0011101000
    print(s.crackSafe(2, 3))  # 0221120100
