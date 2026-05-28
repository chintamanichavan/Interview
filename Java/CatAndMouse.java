import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class CatAndMouse {
    private static final int DRAW = 0, MOUSE = 1, CAT = 2;

    public int catMouseGame(int[][] graph) {
        int n = graph.length;
        int[][][] color = new int[n][n][3];
        int[][][] degree = new int[n][n][3];
        boolean[] hasZero = new boolean[n];
        for (int i = 0; i < n; i++) {
            for (int v : graph[i]) if (v == 0) { hasZero[i] = true; break; }
        }
        for (int m = 0; m < n; m++) {
            for (int c = 0; c < n; c++) {
                degree[m][c][MOUSE] = graph[m].length;
                degree[m][c][CAT] = graph[c].length - (hasZero[c] ? 1 : 0);
            }
        }

        Deque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int t : new int[] { MOUSE, CAT }) {
                color[0][i][t] = MOUSE;
                q.add(new int[] { 0, i, t, MOUSE });
                if (i > 0) {
                    color[i][i][t] = CAT;
                    q.add(new int[] { i, i, t, CAT });
                }
            }
        }

        while (!q.isEmpty()) {
            int[] s = q.poll();
            int m = s[0], c = s[1], turn = s[2], result = s[3];
            if (turn == MOUSE) {
                for (int pc : graph[c]) {
                    if (pc == 0 || color[m][pc][CAT] != DRAW) continue;
                    if (result == CAT) {
                        color[m][pc][CAT] = CAT;
                        q.add(new int[] { m, pc, CAT, CAT });
                    } else if (--degree[m][pc][CAT] == 0) {
                        color[m][pc][CAT] = result;
                        q.add(new int[] { m, pc, CAT, result });
                    }
                }
            } else {
                for (int pm : graph[m]) {
                    if (color[pm][c][MOUSE] != DRAW) continue;
                    if (result == MOUSE) {
                        color[pm][c][MOUSE] = MOUSE;
                        q.add(new int[] { pm, c, MOUSE, MOUSE });
                    } else if (--degree[pm][c][MOUSE] == 0) {
                        color[pm][c][MOUSE] = result;
                        q.add(new int[] { pm, c, MOUSE, result });
                    }
                }
            }
        }

        return color[1][2][MOUSE];
    }

    public static void main(String[] args) {
        CatAndMouse s = new CatAndMouse();
        System.out.println(s.catMouseGame(new int[][] { {2, 5}, {3}, {0, 4, 5}, {1, 4, 5}, {2, 3}, {0, 2, 3} })); // 0
        System.out.println(s.catMouseGame(new int[][] { {1, 3}, {0}, {3}, {0, 2} }));                              // 1
    }
}
