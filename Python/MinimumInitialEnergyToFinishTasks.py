class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Greedy: schedule tasks with the largest (minimum - actual) gap first,
        # so the high-threshold tasks land while remaining energy is highest.
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        total = 0
        spent = 0
        for actual, minimum in tasks:
            if spent + minimum > total:
                total = spent + minimum
            spent += actual
        return total
