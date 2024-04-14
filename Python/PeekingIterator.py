class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums.v[self.nums.index]

    def next(self):
        """
        :rtype: int
        """
        return self.nums.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nums.index != len(self.nums.v)
