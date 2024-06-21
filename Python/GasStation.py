from collections import deque

class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        queue = deque(gas[i] - cost[i] for i in range(n))
        start = 0

        while queue:
            curFuel = queue.popleft()
            start = queue[0] if queue else start  # Check if queue is empty before accessing its elements
            while curFuel >= 0:  # Changed to ">= 0" to ensure it always stops at non-positive curFuel
                if not queue:
                    return start
                curFuel += queue.popleft()
            queue.append(curFuel)

        return start if sum(queue) >= 0 else -1

def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    result = s.canCompleteCircuit(gas, cost)
    print(result)

if __name__ == '__main__':
    main()
