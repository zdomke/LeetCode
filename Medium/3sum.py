class Solution(object):
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
    for te in tests:
        res = sol.threeSum(te)
        print(f"{te}: --> {res}")
