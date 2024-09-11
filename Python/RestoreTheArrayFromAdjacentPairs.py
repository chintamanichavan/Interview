class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        from collections import defaultdict

        # Build a graph from the adjacent pairs
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # Find a starting point for the array (node with only one neighbor)
        start = None
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                start = node
                break

        # Reconstruct the array
        result = [start]
        prev = None
        while len(result) < len(graph):
            current = result[-1]
            next_nodes = graph[current]
            next_node = next_nodes[0] if next_nodes[0] != prev else next_nodes[1]
            result.append(next_node)
            prev = current

        return result

