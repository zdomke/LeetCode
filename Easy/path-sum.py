# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, node: Optional[TreeNode], targetSum: int) -> bool:
        if node == None:
            return targetSum == 0
        newSum = targetSum - node.val
        return self.recursion(node.left, newSum) or self.recursion(node.right, newSum)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.recursion(root, targetSum)