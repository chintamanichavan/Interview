import java.util.Arrays;

public class RedundantConnectionII {
    private int[] uf;

    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1];
        int[] cand1 = null, cand2 = null;
        for (int i = 0; i < n; i++) {
            int u = edges[i][0], v = edges[i][1];
            if (parent[v] != 0) {
                cand1 = new int[] { parent[v], v };
                cand2 = new int[] { u, v };
                edges[i][1] = 0;  // disable cand2 in the union pass
            } else {
                parent[v] = u;
            }
        }

        uf = new int[n + 1];
        for (int i = 0; i <= n; i++) uf[i] = i;
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            if (v == 0) continue;
            int ru = find(u), rv = find(v);
            if (ru == rv) return cand1 != null ? cand1 : new int[] { u, v };
            uf[rv] = ru;
        }
        return cand2;
    }

    private int find(int x) {
        while (uf[x] != x) {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        return x;
    }

    public static void main(String[] args) {
        RedundantConnectionII s = new RedundantConnectionII();
        System.out.println(Arrays.toString(s.findRedundantDirectedConnection(
                new int[][] { {1, 2}, {1, 3}, {2, 3} })));                          // [2, 3]
        System.out.println(Arrays.toString(s.findRedundantDirectedConnection(
                new int[][] { {1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5} })));          // [4, 1]
        System.out.println(Arrays.toString(s.findRedundantDirectedConnection(
                new int[][] { {2, 1}, {3, 1}, {4, 2}, {1, 4} })));                  // [2, 1]
    }
}
