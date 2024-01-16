import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # Swap with the last element
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.dict[last_element] = idx
        # Remove the last element
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
