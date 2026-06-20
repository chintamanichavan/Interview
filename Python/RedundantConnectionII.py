from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # A rooted tree + one extra edge creates one of: (a) a node with two parents, (b) a cycle,
        # or (c) both. Find the two candidate edges pointing into a 2-parent node. Then union-find
        # ignoring cand2: if a cycle still forms, the culprit is the cycle edge (or cand1 if a
        # 2-parent node existed); otherwise it's cand2.
        n = len(edges)
        parent = [0] * (n + 1)  # parent[v] in the input (for detecting two-parents)
        cand1 = cand2 = None
        for i, (u, v) in enumerate(edges):
            if parent[v] != 0:
                cand1 = [parent[v], v]  # earlier edge into v
                cand2 = [u, v]  # this edge into v
                edges[i][1] = 0  # disable cand2 in the union pass
            else:
                parent[v] = u

        uf = list(range(n + 1))

        def find(x: int) -> int:
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        for u, v in edges:
            if v == 0:
                continue
            ru, rv = find(u), find(v)
            if ru == rv:
                # a cycle exists with cand2 removed
                return cand1 if cand1 else [u, v]
            uf[rv] = ru

        return cand2


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))  # [2, 3]
    print(
        s.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]])
    )  # [4, 1]
    print(s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]))  # [2, 1]
