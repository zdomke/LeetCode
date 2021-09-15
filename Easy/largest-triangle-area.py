class Solution:     # 124ms
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = -1
        for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(points, 3):
            maxArea = max(maxArea, .5 * abs(xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc))
        return maxArea