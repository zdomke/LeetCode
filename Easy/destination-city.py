class Solution:     # 73ms
    def destCity(self, paths: List[List[str]]) -> str:
        city = []
        dest = []
        for path in paths:
            city.append(path[0])
            dest.append(path[1])
        return (set(dest) - set(city)).pop()