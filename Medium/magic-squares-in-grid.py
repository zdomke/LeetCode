class Solution(object):
    def numMagicSquaresInside(self, grid: list):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        ret = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                r = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        r.add(grid[k][l])

                if r != set(range(1, 10)):
                    continue

                magic = (
                    (grid[i][j] + grid[i][j + 1] + grid[i][j + 2])
                    == (grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2])
                    == (grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2])
                    == (grid[i][j] + grid[i + 1][j] + grid[i + 2][j])
                    == (grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1])
                    == (grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2])
                    == (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j])
                    == (grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2])
                )
                ret += int(magic)

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], [[8]]]
    for te in tests:
        res = sol.numMagicSquaresInside(te)
        print(f"{te}: --> {res}")
