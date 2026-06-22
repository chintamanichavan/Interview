import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringJoiner;

public class SerializeAndDeserializeBinaryTree {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    static class Codec {
        // Level-order encoding: node value, or '#' for a missing child.
        public String serialize(TreeNode root) {
            if (root == null) return "";
            StringJoiner sj = new StringJoiner(",");
            Queue<TreeNode> q = new LinkedList<>();  // LinkedList tolerates null children
            q.add(root);
            while (!q.isEmpty()) {
                TreeNode node = q.poll();
                if (node != null) {
                    sj.add(Integer.toString(node.val));
                    q.add(node.left);
                    q.add(node.right);
                } else {
                    sj.add("#");
                }
            }
            return sj.toString();
        }

        public TreeNode deserialize(String data) {
            if (data.isEmpty()) return null;
            String[] tokens = data.split(",");
            TreeNode root = new TreeNode(Integer.parseInt(tokens[0]));
            Queue<TreeNode> q = new ArrayDeque<>();
            q.add(root);
            int i = 1;
            while (!q.isEmpty()) {
                TreeNode node = q.poll();
                if (!tokens[i].equals("#")) {
                    node.left = new TreeNode(Integer.parseInt(tokens[i]));
                    q.add(node.left);
                }
                i++;
                if (!tokens[i].equals("#")) {
                    node.right = new TreeNode(Integer.parseInt(tokens[i]));
                    q.add(node.right);
                }
                i++;
            }
            return root;
        }
    }

    static String toList(TreeNode root) {
        // BFS that tolerates nulls (plain ArrayList-backed indices, not ArrayDeque).
        List<TreeNode> level = new ArrayList<>();
        List<String> out = new ArrayList<>();
        level.add(root);
        int idx = 0;
        while (idx < level.size()) {
            TreeNode node = level.get(idx++);
            if (node != null) {
                out.add(Integer.toString(node.val));
                level.add(node.left);
                level.add(node.right);
            } else {
                out.add("null");
            }
        }
        while (!out.isEmpty() && out.get(out.size() - 1).equals("null")) out.remove(out.size() - 1);
        return out.toString();
    }

    public static void main(String[] args) {
        Codec c = new Codec();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);
        String data = c.serialize(root);
        System.out.println(data);
        System.out.println(toList(c.deserialize(data)));  // [1, 2, 3, null, null, 4, 5]
        System.out.println("\"" + c.serialize(c.deserialize(c.serialize(null))) + "\"");  // ""
        System.out.println(toList(c.deserialize(c.serialize(new TreeNode(7)))));  // [7]
    }
}
