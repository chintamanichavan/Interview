class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        current_winner = arr[0]
        win_count = 0
        max_element = current_winner
        
        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                win_count = 1
            else:
                win_count += 1
            
            # Update max_element
            max_element = max(max_element, arr[i])
            
            # Check if current_winner has won k consecutive rounds
            if win_count == k:
                return current_winner
        
        # If no element has won k consecutive rounds, return max_element
        return max_element
