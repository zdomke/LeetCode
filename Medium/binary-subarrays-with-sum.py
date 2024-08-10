class Solution(object):
    def numSubarraysWithSum(self, nums: list, goal: int):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        ret = 0
        curr = 0
        count = {0: 1}

        for n in nums:
            curr += n
            if curr - goal in count:
                ret += count[curr - goal]
            count[curr] = count.get(curr, 0) + 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [[[1, 0, 1, 0, 1], 2], [[0, 0, 0, 0, 0], 0]]
    for te in tests:
        res = sol.numSubarraysWithSum(*te)
        print(f"{te}: --> {res}")
