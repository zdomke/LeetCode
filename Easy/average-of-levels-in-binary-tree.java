/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> ret = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while(!q.isEmpty()){
            long sum = 0, count = 0;
            Queue<TreeNode> temp = new LinkedList<>();
            while(!q.isEmpty()){
                TreeNode node = q.remove();
                sum += node.val;
                count++;
                if(node.left != null)
                    temp.add(node.left);
                if(node.right != null)
                    temp.add(node.right);
            }
            q = temp;
            ret.add(1.0 * sum / count);
        }
        return ret;
    }
}