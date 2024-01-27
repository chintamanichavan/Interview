class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a graph where each node is a bus route and edges exist between routes that share stops
        graph = defaultdict(set)
        stop_to_route = defaultdict(set)
        
        # Map each stop to all routes that contain this stop
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)

        # Create edges between all routes that share at least one stop
        for routes_with_common_stop in stop_to_route.values():
            for route1 in routes_with_common_stop:
                for route2 in routes_with_common_stop:
                    if route1 != route2:
                        graph[route1].add(route2)

        # BFS to find the shortest path from a route containing the source to a route containing the target
        visited = set()
        queue = deque()
        
        # Initialize the queue with all routes that contain the source stop
        for route in stop_to_route[source]:
            queue.append((route, 1))  # (route index, number of buses taken)
            visited.add(route)

        while queue:
            route, buses = queue.popleft()
            
            # Check if this route contains the target
            if target in routes[route]:
                return buses

            # Visit all neighboring routes
            for neighbor in graph[route]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, buses + 1))

        return -1  # Target is not reachable
