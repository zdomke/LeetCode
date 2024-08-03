class Solution(object):
    def findIntersectionValues(self, nums1: list, nums2: list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = sum([nums1.count(n) for n in set(nums2)])
        s2 = sum([nums2.count(n) for n in set(nums1)])

        return [s1, s2]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 3, 2], [1, 2]),
        ([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]),
        ([3, 4, 2, 3], [1, 5])
    ]
    for te in tests:
        res = sol.findIntersectionValues(*te)
        print(f"{te}: --> {res}")
