/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {        // 6ms
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int small = Math.min(p.val, q.val);
        int big = Math.max(p.val, q.val);
        TreeNode ret = root;
        
        while(small > root.val || big < root.val){
            if(small > root.val){
                root = root.right;
            } else {
                root = root.left;
            }
            ret = root;
        }
        return ret;
    }
}