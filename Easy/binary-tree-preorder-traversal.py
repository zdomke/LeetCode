# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return ([root.val]
                + self.preorderTraversal(root.left)
                + self.preorderTraversal(root.right))

    def iterativeTraversal(self, root):
        if not root:
            return []

        ret = []
        tree_stack = [root]

        while tree_stack:
            node = tree_stack.pop()
            if node:
                ret.append(node.val)
                tree_stack.append(node.right)
                tree_stack.append(node.left)
        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [[1, None, 2, 3],
             [],
             [1]]
    for te in tests:
        res = sol.preorderTraversal(*te)
        print(f"{te}: --> {res}")
