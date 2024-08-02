class Solution(object):
    def minSwaps(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        long_nums = nums + nums
        start = 0
        end = nums.count(1)
        curr_zero = nums[:end].count(0)
        ret = curr_zero
        while start < len(nums):
            curr_zero += 1 if not long_nums[end] else 0
            curr_zero -= 1 if not long_nums[start] else 0
            ret = min(ret, curr_zero)

            start += 1
            end += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [0, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
    ]
    for te in tests:
        res = sol.minSwaps(te)
        print(f"{te}: --> {res}")
