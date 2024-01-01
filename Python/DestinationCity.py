class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        departure_cities = set()
        
        # Add all departure cities to the set
        for path in paths:
            departure_cities.add(path[0])
        
        # Find the destination city
        for path in paths:
            if path[1] not in departure_cities:
                return path[1]
