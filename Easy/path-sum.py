# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, node: Optional[TreeNode], targetSum: int) -> bool:
        if node.left == None and node.right == None:
            return node.val == targetSum
        left = False
        if(node.left != None):
            left = self.recursion(node.left, targetSum - node.val)
        right = False
        if(node.right != None):
            right = self.recursion(node.right, targetSum - node.val)
        return left or right
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.recursion(root, targetSum)