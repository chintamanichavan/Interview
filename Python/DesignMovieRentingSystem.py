import bisect
from collections import defaultdict
from typing import List


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # available[movie] = sorted list of (price, shop) for unrented copies.
        # rented = sorted list of (price, shop, movie) across all rented copies.
        # price[(shop, movie)] = price, for O(1) lookup on rent/drop.
        self.available = defaultdict(list)
        self.rented: List[tuple] = []
        self.price = {}
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            bisect.insort(self.available[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        lst = self.available[movie]
        lst.pop(bisect.bisect_left(lst, (p, shop)))
        bisect.insort(self.rented, (p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.rented.pop(bisect.bisect_left(self.rented, (p, shop, movie)))
        bisect.insort(self.available[movie], (p, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


def run(ops, args):
    out = []
    sys = None
    for op, a in zip(ops, args):
        if op == "MovieRentingSystem":
            sys = MovieRentingSystem(a[0], a[1])
            out.append("null")
        elif op == "search":
            out.append(str(sys.search(a[0])))
        elif op == "rent":
            sys.rent(a[0], a[1])
            out.append("null")
        elif op == "drop":
            sys.drop(a[0], a[1])
            out.append("null")
        elif op == "report":
            out.append(str(sys.report()))
    return "[" + ", ".join(out) + "]"


if __name__ == '__main__':
    ops = ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
    args = [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]],
            [1], [0, 1], [1, 2], [], [1, 2], [2]]
    print(run(ops, args))
    # [null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
