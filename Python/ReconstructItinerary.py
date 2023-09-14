from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list to represent the graph
        graph = {}
        for ticket in tickets:
            from_i, to_i = ticket
            if from_i in graph:
                graph[from_i].append(to_i)
            else:
                graph[from_i] = [to_i]

        # Sort the destinations in lexical order for each airport
        for airport in graph:
            graph[airport].sort()

        def dfs(airport):
            if airport in graph:
                destinations = graph[airport]
                while destinations:
                    next_destination = destinations.pop(0)
                    dfs(next_destination)
                # After visiting all destinations, prepend the current airport to the result
            result.insert(0, airport)

        # Initialize the result list
        result = []

        # Start the DFS from "JFK"
        dfs("JFK")

        return result

def main():
    s = Solution()
    # Example usage:
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(s.findItinerary(tickets1))  # Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(s.findItinerary(tickets2))  # Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

if __name__ == '__main__':
    main()
