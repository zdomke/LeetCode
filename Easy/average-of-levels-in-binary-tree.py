# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     # 44ms
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = []
        q.append(root)
        
        while q:
            sum = 0
            count = 0
            temp = []
            while q:
                node = q.pop()
                sum += node.val
                count += 1
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            q = temp
            res.append(sum / count)
        return res