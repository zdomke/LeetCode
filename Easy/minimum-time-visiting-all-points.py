class Solution:     # 77ms
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        curr = points[0]
        for point in points:
            t += max(abs(point[0] - curr[0]), abs(point[1] - curr[1]))
            curr = point
        return t