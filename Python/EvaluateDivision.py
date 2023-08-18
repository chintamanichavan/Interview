class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.weight = {}

    def find(self, x):
        if x != self.parent.get(x, x):
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[self.parent[x]]
        return self.parent.get(x, x)

    def union(self, x, y, value):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            self.parent[xr] = yr
            self.weight[xr] = self.weight[y] * 1 / (self.weight[x] / value)

    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for (x, y), v in zip(equations, values):
            uf.union(x, y, v)

        res = []
        for q in queries:
            if q[0] not in uf.parent or q[1] not in uf.parent:
                res.append(-1.0)
            elif uf.find(q[0]) != uf.find(q[1]):
                res.append(-1.0)
            else:
                res.append(uf.weight[q[0]] / uf.weight[q[1]])

        return res

def main():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    s = UnionFind()
    res = s.calcEquation(equations, values, queries)
    print(res)

if __name__ == '__main__':
    main()
