class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import Counter

        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_frequency_count = list(task_counts.values()).count(max_frequency)

        return max((max_frequency - 1) * (n + 1) + max_frequency_count, len(tasks))
