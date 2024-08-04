class Solution(object):
    def rangeSum(self, nums: list, n: int, left: int, right: int):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        arr = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                arr.append(curr)

        arr.sort()
        return sum(arr[left-1:right]) % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], 4, 1, 5),
        ([1, 2, 3, 4], 4, 3, 4),
        ([1, 2, 3, 4], 4, 1, 10)
    ]
    for te in tests:
        res = sol.rangeSum(*te)
        print(f"{te}: --> {res}")
