# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ret = 0
        if root.left and not root.left.left and not root.left.right:
            ret = root.left.val

        ret += self.sumOfLeftLeaves(root.left)
        ret += self.sumOfLeftLeaves(root.right)

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [3, 9, 20, None, None, 15, 7],
        [1],
    ]
    for te in tests:
        res = sol.sumOfLeftLeaves(*te)
        print(f"{te}: --> {res}")
