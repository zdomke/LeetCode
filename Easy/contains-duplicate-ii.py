class Solution(object):
    def containsNearbyDuplicate(self, nums: list, k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for i, n in enumerate(nums):
            if n in d:
                if i - d[n] <= k:
                    return True
            d[n] = i

        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2)
    ]
    for te in tests:
        res = sol.containsNearbyDuplicate(*te)
        print(f"{te}: --> {res}")
