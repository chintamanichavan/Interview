import java.util.ArrayList;
import java.util.List;

public class MaximumPathQualityOfAGraph {
    private List<int[]>[] adj;   // node -> [to, cost]
    private int[] values;
    private int[] visited;
    private long best;

    @SuppressWarnings("unchecked")
    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {
        int n = values.length;
        this.values = values;
        adj = new List[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[] { e[1], e[2] });
            adj[e[1]].add(new int[] { e[0], e[2] });
        }
        visited = new int[n];
        best = 0;
        visited[0] = 1;
        dfs(0, maxTime, values[0]);
        return (int) best;
    }

    private void dfs(int node, int timeLeft, long quality) {
        if (node == 0 && quality > best) best = quality;
        for (int[] e : adj[node]) {
            int to = e[0], cost = e[1];
            if (cost <= timeLeft) {
                long gain = visited[to] == 0 ? values[to] : 0;
                visited[to]++;
                dfs(to, timeLeft - cost, quality + gain);
                visited[to]--;
            }
        }
    }

    public static void main(String[] args) {
        MaximumPathQualityOfAGraph s = new MaximumPathQualityOfAGraph();
        System.out.println(s.maximalPathQuality(new int[] { 0, 32, 10, 43 },
                new int[][] { {0, 1, 10}, {1, 2, 15}, {0, 3, 10} }, 49));  // 75
        System.out.println(s.maximalPathQuality(new int[] { 5, 10, 15, 20 },
                new int[][] { {0, 1, 10}, {1, 2, 10}, {0, 3, 10} }, 30));  // 25
        System.out.println(s.maximalPathQuality(new int[] { 1, 2, 3, 4 },
                new int[][] { {0, 1, 10}, {1, 2, 11}, {2, 3, 12}, {1, 3, 13} }, 50));  // 7
        System.out.println(s.maximalPathQuality(new int[] { 5 }, new int[][] {}, 100));  // 5
    }
}
