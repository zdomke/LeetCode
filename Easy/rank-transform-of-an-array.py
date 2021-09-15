class Solution:     # 344ms
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        a = []
        for i in sorted(arr):
            if i not in rank:
                rank[i] = len(rank) + 1
        for i in arr:
            a.append(rank[i])
                
        return a