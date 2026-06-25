from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        # BFS over (position, speed). 'A': pos += speed, speed *= 2. 'R': speed = -1 if speed>0
        # else 1 (position unchanged). Shortest instruction count to reach target. Positions are
        # bounded to [-2*target, 2*target] since overshooting past 2*target never helps.
        bound = 2 * target
        start = (0, 1)
        seen = {start}
        queue = deque([(0, 1, 0)])  # pos, speed, steps
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            # 'A'
            npos, nspeed = pos + speed, speed * 2
            if -bound <= npos <= bound and (npos, nspeed) not in seen:
                seen.add((npos, nspeed))
                queue.append((npos, nspeed, steps + 1))
            # 'R'
            nspeed = -1 if speed > 0 else 1
            if (pos, nspeed) not in seen:
                seen.add((pos, nspeed))
                queue.append((pos, nspeed, steps + 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.racecar(3))  # 2  ("AA")
    print(s.racecar(6))  # 5  ("AAARA")
    print(s.racecar(1))  # 1  ("A")
    print(s.racecar(4))  # 5
