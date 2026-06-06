import heapq
from typing import List


class DinnerPlates:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks: List[List[int]] = []
        self.avail: List[int] = []  # min-heap of indices with room (may hold stale entries)

    def push(self, val: int) -> None:
        # Drop stale indices: out of range or already full.
        while self.avail and (self.avail[0] >= len(self.stacks)
                              or len(self.stacks[self.avail[0]]) >= self.cap):
            heapq.heappop(self.avail)
        if not self.avail:
            heapq.heappush(self.avail, len(self.stacks))
            self.stacks.append([])
        i = self.avail[0]
        self.stacks[i].append(val)
        if len(self.stacks[i]) >= self.cap:
            heapq.heappop(self.avail)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        heapq.heappush(self.avail, index)  # this stack now has room
        return self.stacks[index].pop()


def run(ops, args):
    out = []
    d = None
    for op, a in zip(ops, args):
        if op == "DinnerPlates":
            d = DinnerPlates(a[0])
            out.append("null")
        elif op == "push":
            d.push(a[0])
            out.append("null")
        elif op == "pop":
            out.append(str(d.pop()))
        elif op == "popAtStack":
            out.append(str(d.popAtStack(a[0])))
    return "[" + ", ".join(out) + "]"


if __name__ == '__main__':
    ops = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
           "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
    args = [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
    print(run(ops, args))
    # [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
