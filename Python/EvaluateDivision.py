from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        # Weighted union-find. weight[x] holds x / parent[x]; after find with path
        # compression it holds x / root. Nodes are lazily initialized on first find.
        parent: dict[str, str] = {}
        weight: dict[str, float] = {}

        def find(x: str) -> str:
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
                return x
            if parent[x] != x:
                orig = parent[x]
                parent[x] = find(orig)
                weight[x] *= weight[orig]
            return parent[x]

        def union(x: str, y: str, value: float) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # x / y = value, with x = weight[x]*rx and y = weight[y]*ry, so
            # rx / ry = value * weight[y] / weight[x]. Attach rx under ry.
            parent[rx] = ry
            weight[rx] = value * weight[y] / weight[x]

        for (x, y), v in zip(equations, values):
            union(x, y, v)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent or find(a) != find(b):
                res.append(-1.0)
            else:
                res.append(weight[a] / weight[b])
        return res


def main():
    s = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(s.calcEquation(equations, values, queries))  # [6.0, 0.5, -1.0, 1.0, -1.0]


if __name__ == '__main__':
    main()
