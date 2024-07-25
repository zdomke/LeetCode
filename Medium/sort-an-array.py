class Solution(object):
    def sortArray(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums

        ind = len(nums) // 2
        left = self.sortArray(nums[:ind])
        right = self.sortArray(nums[ind:])
        return self.combine_arrs(left, right)

    def combine_arrs(self, l1, l2):
        ret = []
        while True:
            ret.append(l1.pop(0) if l1[0] <= l2[0] else l2.pop(0))
            if not l1:
                ret += l2
                break
            elif not l2:
                ret += l1
                break
        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [([5, 2, 3, 1],),
             ([5, 1, 1, 2, 0, 0],)]
    for te in tests:
        res = sol.sortArray(*te)
        print(f"{te}: --> {res}")
