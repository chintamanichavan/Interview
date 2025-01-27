class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, values, index=0):
        if index < len(values) and values[index] is not None:
            node = TreeNode(values[index])
            node.left = self.buildTree(values, 2 * index + 1)
            node.right = self.buildTree(values, 2 * index + 2)
            return node
        return None

    def convertToGraph(self, node, graph, parent=None):
        if node:
            if parent:
                graph[node.val].add(parent.val)
                graph[parent.val].add(node.val)
            self.convertToGraph(node.left, graph, node)
            self.convertToGraph(node.right, graph, node)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        self.convertToGraph(root, graph)

        visited = set()
        queue = deque([(start, 0)])
        maxTime = 0

        while queue:
            node, time = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            maxTime = time

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, time + 1))

        return maxTime
