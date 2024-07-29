class Solution(object):
    def numTeams(self, rating: list):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0
        n = len(rating)

        for j in range(1, n-1):
            x, left_lo, left_hi, right_lo, right_hi = rating[j], 0, 0, 0, 0

            for i in range(j):
                if rating[i] < x:
                    left_lo += 1
                elif rating[i] > x:
                    left_hi += 1

            for k in range(j+1, n):
                if rating[k] < x:
                    right_lo += 1
                elif rating[k] > x:
                    right_hi += 1

            count += left_lo * right_hi + left_hi * right_lo

        return count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 5, 3, 4, 1]),
        ([2, 1, 3]),
        ([1, 2, 3, 4])
    ]
    for te in tests:
        res = sol.numTeams(te)
        print(f"{te}: --> {res}")
