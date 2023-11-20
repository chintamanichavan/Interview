class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
         
        # Last seen house indices for each type of garbage
        last_M, last_P, last_G = -1, -1, -1

        # Total collection time for each type of garbage
        total_M, total_P, total_G = 0, 0, 0

        # Iterate through each house to find the last house with each type of garbage and total collection time
        for i, g in enumerate(garbage):
            if 'M' in g:
                last_M = i
                total_M += g.count('M')
            if 'P' in g:
                last_P = i
                total_P += g.count('P')
            if 'G' in g:
                last_G = i
                total_G += g.count('G')

        # Calculate the total travel time for each truck
        travel_time_M = sum(travel[:last_M]) if last_M != -1 else 0
        travel_time_P = sum(travel[:last_P]) if last_P != -1 else 0
        travel_time_G = sum(travel[:last_G]) if last_G != -1 else 0

        return total_M + total_P + total_G + travel_time_M + travel_time_P + travel_time_G
