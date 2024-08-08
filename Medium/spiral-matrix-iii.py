class Solution(object):
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        visit = [[rStart, cStart]]
        steps = 1
        direction = 1   # 1 => right/down; -1 => left/up

        r, c = rStart, cStart
        while len(visit) < (rows * cols):
            for _ in range(steps):
                c += direction
                if 0 <= r < rows and 0 <= c < cols:
                    visit.append([r, c])

            for _ in range(steps):
                r += direction
                if 0 <= r < rows and 0 <= c < cols:
                    visit.append([r, c])

            steps += 1
            direction *= -1

        return visit


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, 4, 0, 0),
        (5, 6, 1, 4)
    ]
    for te in tests:
        res = sol.spiralMatrixIII(*te)
        print(f"{te}: --> {res}")
