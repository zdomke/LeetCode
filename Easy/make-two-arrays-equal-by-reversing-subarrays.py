class Solution(object):
    def canBeEqual(self, target: list, arr: list):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return sorted(target) == sorted(arr)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], [2, 4, 1, 3]),
        ([7], [7]),
        ([3, 7, 9], [3, 7, 11])
    ]
    for te in tests:
        res = sol.canBeEqual(*te)
        print(f"{te}: --> {res}")
