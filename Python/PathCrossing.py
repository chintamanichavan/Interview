class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Starting at the origin
        x, y = 0, 0
        # Set to keep track of visited points
        visited = {(x, y)}

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            # Check if the new position has been visited before
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
