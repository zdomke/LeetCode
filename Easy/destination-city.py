class Solution:     # 52ms
    def destCity(self, paths: List[List[str]]) -> str:
        city, dest = map(set, zip(*paths))
        return (dest - city).pop()