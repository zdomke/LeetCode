class Solution(object):
    def removeElement(self, nums: list, val: int):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind


if __name__ == "__main__":
    sol = Solution()
    tests = [([3, 2, 2, 3], 3),
             ([0, 1, 2, 2, 3, 0, 4, 2], 2)]
    for te in tests:
        print(f"{te} --> {sol.removeElement(*te)}")
