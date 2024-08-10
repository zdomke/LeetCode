class Solution(object):
    def productExceptSelf(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [1] * n

        left = 1
        for i in range(n):
            ret[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= right
            right *= nums[i]

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3]
    ]
    for te in tests:
        res = sol.productExceptSelf(te)
        print(f"{te}: --> {res}")
