class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        from itertools import product
        m, n = len(mat), len(mat[0])

        prefix = [[0]*(n+1) for _ in range(m+1)]

        for i, j in product(range(m), range(n)):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + mat[i][j]

        def below(k):
            for i, j in product(range(m + 1 - k), range(n + 1 - k)):
                if prefix[i+k][j+k] - prefix[i][j+k] - prefix[i+k][j] + prefix[i][j] <= threshold: return True
            return False


        lo, hi = 1, min(m, n)
        while lo <= hi:
            mid = (lo + hi) // 2
            if below(mid): lo = mid + 1
            else: hi = mid - 1
        return hi