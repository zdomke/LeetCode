class Solution(object):
    def mostPoints(self, questions: list):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        ans = [0] * (len(questions) + 1)
        for i in range(len(questions) - 1, -1, -1):
            pt, bp = questions[i]
            next_q = i + bp + 1
            next_q = min(next_q, len(questions))
            ans[i] = max(ans[i+1], pt + ans[next_q])
        return ans[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [[[3, 2], [4, 3], [4, 4], [2, 5]],
             [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
             [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]],
             [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]]
    for te in tests:
        res = sol.mostPoints(te)
        print(f"{te}: --> {res}")
