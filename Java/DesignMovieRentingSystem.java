import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringJoiner;
import java.util.TreeSet;

public class DesignMovieRentingSystem {
    static class MovieRentingSystem {
        // available[movie] = sorted set of {price, shop}; rented = sorted set of {price, shop, movie}.
        private final Map<Integer, TreeSet<int[]>> available = new HashMap<>();
        private final TreeSet<int[]> rented = new TreeSet<>(
                Comparator.<int[]>comparingInt(a -> a[0]).thenComparingInt(a -> a[1]).thenComparingInt(a -> a[2]));
        private final Map<Long, Integer> price = new HashMap<>();

        private static final Comparator<int[]> BY_PRICE_SHOP =
                Comparator.<int[]>comparingInt(a -> a[0]).thenComparingInt(a -> a[1]);

        MovieRentingSystem(int n, int[][] entries) {
            for (int[] e : entries) {
                int shop = e[0], movie = e[1], p = e[2];
                price.put(key(shop, movie), p);
                available.computeIfAbsent(movie, k -> new TreeSet<>(BY_PRICE_SHOP)).add(new int[] { p, shop });
            }
        }

        List<Integer> search(int movie) {
            List<Integer> res = new ArrayList<>();
            TreeSet<int[]> set = available.get(movie);
            if (set != null) {
                for (int[] e : set) {
                    if (res.size() == 5) break;
                    res.add(e[1]);
                }
            }
            return res;
        }

        void rent(int shop, int movie) {
            int p = price.get(key(shop, movie));
            available.get(movie).remove(new int[] { p, shop });
            rented.add(new int[] { p, shop, movie });
        }

        void drop(int shop, int movie) {
            int p = price.get(key(shop, movie));
            rented.remove(new int[] { p, shop, movie });
            available.get(movie).add(new int[] { p, shop });
        }

        List<List<Integer>> report() {
            List<List<Integer>> res = new ArrayList<>();
            for (int[] e : rented) {
                if (res.size() == 5) break;
                res.add(List.of(e[1], e[2]));
            }
            return res;
        }

        private static long key(int shop, int movie) {
            return (long) shop * 100000 + movie;
        }
    }

    public static void main(String[] args) {
        int[][] entries = { {0, 1, 5}, {0, 2, 6}, {0, 3, 7}, {1, 1, 4}, {1, 2, 7}, {2, 1, 5} };
        MovieRentingSystem m = new MovieRentingSystem(3, entries);
        StringJoiner sj = new StringJoiner(", ", "[", "]");
        sj.add("null");
        sj.add(m.search(1).toString());
        m.rent(0, 1);
        sj.add("null");
        m.rent(1, 2);
        sj.add("null");
        sj.add(m.report().toString());
        m.drop(1, 2);
        sj.add("null");
        sj.add(m.search(2).toString());
        System.out.println(sj);
    }
}
