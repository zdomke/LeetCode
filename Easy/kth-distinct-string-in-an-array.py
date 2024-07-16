class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        dist = 0
        for s in arr:
            dist = dist + 1 if arr.count(s) == 1 else dist
            if dist == k: return s
        return ""