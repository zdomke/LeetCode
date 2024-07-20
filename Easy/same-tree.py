from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif (p and not q) or (not p and q) or p.val != q.val:
            return False

        if p.left and q.left or not (p.left or q.left):
            left_ch = self.isSameTree(p.left, q.left)
        else:
            return False

        if p.right and q.right or not (p.right or q.right):
            right_ch = self.isSameTree(p.right, q.right)
        else:
            return False

        return p.val == q.val and left_ch and right_ch


if __name__ == "__main__":
    sol = Solution()
    tests = [([1, 2, 3], [1, 2, 3]),
             ([1, 2], [1, None, 2]),
             ([1, 2, 1], [1, 1, 2])]
    for te in tests:
        print(f"{te} --> {sol.isSameTree(*te)}")
