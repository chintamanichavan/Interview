class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time_taken = {}
        incoming = [0] * n
        graph = {i:[] for i in range(n)}
        for i in range(len(relations)):
            pre,cour = relations[i]
            graph[pre-1].append(cour-1)
            incoming[cour-1] += 1

        que = deque([])
        tot_time = [0] * n

        for node in range(n):
            if incoming[node] == 0:
                que.append(node)
                tot_time[node] = time[node]
        while que:
            node = que.popleft()
            for neigh in graph[node]:
                tot_time[neigh] = max(tot_time[node] + time[neigh], tot_time[neigh])
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    que.append(neigh)
        return max(tot_time)    
