class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Calculate the time it takes for each monster to reach the city
        time_to_city = [(dist[i] - 1) / speed[i] for i in range(len(dist))]
        
        # Sort the times in ascending order
        time_to_city.sort()
        
        # Start at time 0 and count the number of monsters we can eliminate
        time = 0
        monsters_eliminated = 0
        for t in time_to_city:
            if t >= time:  # Check if we can eliminate the monster before it reaches the city
                monsters_eliminated += 1
                time += 1
            else:  # If the monster would reach the city before we can eliminate it, we lose
                break
        
        return monsters_eliminated
