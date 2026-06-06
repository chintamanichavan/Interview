import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringJoiner;

public class DinnerPlateStacks {
    static class DinnerPlates {
        private final int cap;
        private final List<List<Integer>> stacks = new ArrayList<>();
        private final PriorityQueue<Integer> avail = new PriorityQueue<>();  // min-heap of indices

        DinnerPlates(int capacity) {
            this.cap = capacity;
        }

        void push(int val) {
            while (!avail.isEmpty()
                    && (avail.peek() >= stacks.size() || stacks.get(avail.peek()).size() >= cap)) {
                avail.poll();
            }
            if (avail.isEmpty()) {
                avail.add(stacks.size());
                stacks.add(new ArrayList<>());
            }
            int i = avail.peek();
            stacks.get(i).add(val);
            if (stacks.get(i).size() >= cap) avail.poll();
        }

        int pop() {
            while (!stacks.isEmpty() && stacks.get(stacks.size() - 1).isEmpty()) {
                stacks.remove(stacks.size() - 1);
            }
            if (stacks.isEmpty()) return -1;
            return popAtStack(stacks.size() - 1);
        }

        int popAtStack(int index) {
            if (index >= stacks.size() || stacks.get(index).isEmpty()) return -1;
            avail.add(index);
            List<Integer> s = stacks.get(index);
            return s.remove(s.size() - 1);
        }
    }

    public static void main(String[] args) {
        String[] ops = {"DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
                "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"};
        int[] arg = {2, 1, 2, 3, 4, 5, 0, 20, 21, 0, 2, 0, 0, 0, 0, 0};

        DinnerPlates d = null;
        StringJoiner sj = new StringJoiner(", ", "[", "]");
        for (int i = 0; i < ops.length; i++) {
            switch (ops[i]) {
                case "DinnerPlates" -> { d = new DinnerPlates(arg[i]); sj.add("null"); }
                case "push" -> { d.push(arg[i]); sj.add("null"); }
                case "pop" -> sj.add(Integer.toString(d.pop()));
                case "popAtStack" -> sj.add(Integer.toString(d.popAtStack(arg[i])));
            }
        }
        System.out.println(sj);
    }
}
