/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {        // 3ms
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int small = Math.min(p.val, q.val);
        int big = Math.max(p.val, q.val);
        
        while(small > root.val || big < root.val){
            root = small > root.val ? root.right : root.left;
        }
        return root;
    }
}