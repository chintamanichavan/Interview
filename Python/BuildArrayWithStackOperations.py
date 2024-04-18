class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        operations = []
        i = 0
        for num in range(1, n+1):
            operations.append("Push")
            if target[i] == num:
                i += 1
            else:
                operations.append("Pop")
            if i == len(target):
                break
        return operations
