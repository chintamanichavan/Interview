import java.util.ArrayList;
import java.util.List;

public class FrogPositionAfterTSeconds {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        return dfs(adj, visited, target, t, 1, 0, 1.0);
    }

    private double dfs(List<List<Integer>> adj, boolean[] visited, int target, int t,
                       int node, int time, double prob) {
        List<Integer> children = new ArrayList<>();
        for (int v : adj.get(node)) if (!visited[v]) children.add(v);
        if (node == target) {
            return (time == t || children.isEmpty()) ? prob : 0.0;
        }
        if (time == t || children.isEmpty()) return 0.0;
        double p = prob / children.size();
        for (int c : children) {
            visited[c] = true;
            double res = dfs(adj, visited, target, t, c, time + 1, p);
            if (res > 0.0) return res;
        }
        return 0.0;
    }

    public static void main(String[] args) {
        FrogPositionAfterTSeconds s = new FrogPositionAfterTSeconds();
        int[][] edges = { {1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5} };
        System.out.println(s.frogPosition(7, edges, 2, 4));   // 0.1666...
        System.out.println(s.frogPosition(7, edges, 1, 7));   // 0.3333...
        System.out.println(s.frogPosition(7, edges, 20, 6));  // 0.1666...
        System.out.println(s.frogPosition(1, new int[0][], 1, 1)); // 1.0
    }
}
