# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     # 80ms
    def helper(self, node: Optional[TreeNode], i, sAvg, count):
        if node is None:
            return
        if i < len(sAvg):
            sAvg[i] += node.val
            count[i] += 1
        else:
            sAvg.append(node.val)
            count.append(1)
        self.helper(node.left, i + 1, sAvg, count)
        self.helper(node.right, i + 1, sAvg, count)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sAvg = []
        count = []
        self.helper(root, 0, sAvg, count)
        return [sAvg[i] / count[i] for i in range(len(sAvg))]