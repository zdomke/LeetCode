class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


if __name__ == "__main__":
    sol = Solution()
    tests = [(2.00000, 10),
             (2.10000, 3),
             (2.00000, -2)]
    for te in tests:
        res = sol.myPow(*te)
        print(f"{te}: --> {res}")
