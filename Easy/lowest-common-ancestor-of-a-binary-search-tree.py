# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:     # 72ms
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p.val, q.val)
        big = max(p.val, q.val)
        st = [root]
        while small > root.val or big < root.val:
            if small > root.val:
                root = root.right
            else:
                root = root.left
            st.append(root)
        return st.pop()