from collections import OrderedDict, defaultdict


class LFUCache:
    # O(1) get/put. Each key maps to (value, freq). Keys are bucketed by frequency in insertion-
    # ordered maps, so the LFU bucket's oldest key is the eviction target (LRU tie-break).
    # min_freq tracks the smallest non-empty bucket.
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(
            OrderedDict
        )  # freq -> {key: None} in insertion order
        self.min_freq = 0

    def _bump(self, key: int) -> None:
        f = self.key_to_freq[key]
        del self.freq_to_keys[f][key]
        if not self.freq_to_keys[f]:
            del self.freq_to_keys[f]
            if self.min_freq == f:
                self.min_freq += 1
        self.key_to_freq[key] = f + 1
        self.freq_to_keys[f + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._bump(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._bump(key)
            return
        if len(self.key_to_val) >= self.cap:
            evict, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict]
            del self.key_to_freq[evict]
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


def run(ops, args):
    out = []
    c = None
    for op, a in zip(ops, args):
        if op == "LFUCache":
            c = LFUCache(a[0])
            out.append("null")
        elif op == "get":
            out.append(str(c.get(a[0])))
        elif op == "put":
            c.put(a[0], a[1])
            out.append("null")
    return "[" + ", ".join(out) + "]"


if __name__ == "__main__":
    ops = [
        "LFUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    print(run(ops, args))
    # [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
