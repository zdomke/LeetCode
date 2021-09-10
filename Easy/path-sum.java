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
class Solution {        // 1ms
    public boolean recursion(TreeNode root, int targetSum) {
        if(root.left == null && root.right == null)
            return root.val == targetSum;
        
        if(root.left != null && recursion(root.left, targetSum - root.val))
            return true;
        
        if(root.right != null && recursion(root.right, targetSum - root.val))
            return true;
        
        return false;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return recursion(root, targetSum);
    }
}