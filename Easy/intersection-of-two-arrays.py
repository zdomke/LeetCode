class Solution(object):
    def intersection(self, nums1: list, nums2: list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1).intersection(set(nums2))
        return list(inter)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4]),
    ]
    for te in tests:
        res = sol.intersection(*te)
        print(f"{te}: --> {res}")
