class Solution(object):
    def pivotInteger(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        left = sum(range(n+1))
        right = n
        curr = n

        while left >= right:
            if left == right:
                return curr

            left -= curr
            curr -= 1
            right += curr

        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        8,
        1,
        4
    ]
    for te in tests:
        res = sol.pivotInteger(te)
        print(f"{te}: --> {res}")
