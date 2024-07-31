class Solution(object):
    def minHeightShelves(self, books: list, shelfWidth: int):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books) + 1
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0

        for i in range(n):
            rem_width = shelfWidth
            max_height = 0
            j = i - 1
            while j >= 0 and rem_width - books[j][0] >= 0:
                rem_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1

        return dp[i]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4),
        ([[1, 3], [2, 4], [3, 2]], 6),
    ]
    for te in tests:
        res = sol.some_solution(*te)
        print(f"{te}: --> {res}")
