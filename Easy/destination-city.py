class Solution:     # 44ms
    def destCity(self, paths: List[List[str]]) -> str:
        dest = set()
        for path in paths:
            dest.add(path[0])
        for path in paths:
            if path[1] not in dest:
                return path[1]