import java.util.Arrays;

public class DestroyingAsteroids {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        // Sum may exceed int32 (~1e10); accumulate in long.
        long m = mass;
        for (int a : asteroids) {
            if (m < a) return false;
            m += a;
        }
        return true;
    }

    public static void main(String[] args) {
        DestroyingAsteroids s = new DestroyingAsteroids();
        System.out.println(s.asteroidsDestroyed(10, new int[] { 3, 9, 19, 5, 21 })); // true
        System.out.println(s.asteroidsDestroyed(5, new int[] { 4, 9, 23, 4 }));      // false
        System.out.println(s.asteroidsDestroyed(1, new int[] { 1 }));                // true
        System.out.println(s.asteroidsDestroyed(1, new int[] { 2 }));                // false
    }
}
