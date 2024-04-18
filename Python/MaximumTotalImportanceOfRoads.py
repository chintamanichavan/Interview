
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Calculate the degree of each city
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        # Step 2: Sort cities by degree in descending order
        city_indices = list(range(n))
        city_indices.sort(key=lambda x: degree[x], reverse=True)

        # Step 3: Assign values from n to 1 based on sorted order
        values = [0] * n
        for i in range(n):
            values[city_indices[i]] = n - i

        # Step 4: Calculate the total importance
        total_importance = 0
        for road in roads:
            total_importance += values[road[0]] + values[road[1]]

        return total_importance

# Example usage:
# sol = Solution()
# print(sol.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # Output: 43
# print(sol.maximumImportance(5, [[0,3],[2,4],[1,3]]))  # Output: 20
