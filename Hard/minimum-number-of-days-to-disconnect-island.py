class Solution(object):
    def minDays(self, grid: list):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if self.island_count(grid) != 1:
            return 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                grid[i][j] = 0

                if self.island_count(grid) != 1:
                    return 1
                grid[i][j] = 1

        return 2

    def dfs(self, grid: list, visited: set, i: int, j: int):
        m, n = len(grid), len(grid[0])

        if not ((0 <= i < m) and (0 <= j < n)) or not grid[i][j] or (i, j) in visited:
            return

        visited.add((i, j))
        self.dfs(grid, visited, i + 1, j)
        self.dfs(grid, visited, i - 1, j)
        self.dfs(grid, visited, i, j + 1)
        self.dfs(grid, visited, i, j - 1)

    def island_count(self, grid: list):
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j] or (i, j) in visited:
                    continue
                count += 1
                if count == 2:
                    return 2
                self.dfs(grid, visited, i, j)

        return count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
        [[1, 1]],
        [[1, 0, 1, 0]],
        [[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]],
    ]
    for te in tests:
        res = sol.minDays(te)
        print(f"{te}: --> {res}")
