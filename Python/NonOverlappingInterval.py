import math
from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    ans = 0
    currentEnd = -math.inf

    for interval in sorted(intervals, key=lambda x: x[1]):
      if interval[0] >= currentEnd:
        currentEnd = interval[1]
      else:
        ans += 1

    return ans

  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
      if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
      else:
        merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

  def main(self, intervals: List[List[int]]) -> int:
    merged_intervals = self.merge(intervals)
    return self.eraseOverlapIntervals(merged_intervals)
