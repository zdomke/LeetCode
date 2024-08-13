class Solution(object):
    def combinationSum2(self, candidates: list, target: int):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: Set[List[int]]
        """
        ret = set()
        candidates.sort()
        n = len(candidates)

        def rec(curr_sum, li, ind):
            if curr_sum > target:
                return
            if curr_sum == target:
                ret.add(tuple(sorted(li)))
                return

            for i in range(ind, n):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                rec(curr_sum + candidates[i], li + [candidates[i]], i + 1)

        rec(0, [], 0)
        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([10, 1, 2, 7, 6, 1, 5], 8),
        ([2, 5, 2, 1, 2], 5),
    ]
    for te in tests:
        res = sol.combinationSum2(*te)
        print(f"{te}: --> {res}")
