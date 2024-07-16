import math

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        ret = -1
        small = math.inf

        for i, (xi, yi) in enumerate(points):
            dx = xi - x
            dy = yi - y
            dist = abs(dx + dy)
            if dx * dy == 0 and dist < small:
                small = dist
                ret = i
        return ret

def main():
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    sol = Solution()

    print(sol.nearestValidPoint(x, y, points))


if __name__ == "__main__":
    main()