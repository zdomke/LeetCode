import java.util.*;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution { // 3ms
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> ret = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            double sum = 0;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                sum += node.val;
                if (node.left != null)
                    q.add(node.left);
                if (node.right != null)
                    q.add(node.right);
            }
            ret.add(sum / size);
        }
        return ret;
    }
}