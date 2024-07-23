class Solution(object):
    def mostPoints(self, questions: list):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        # ans = set()
        # skip = set()

        # for i in range(len(questions)):
        #     if i in skip:
        #         continue
        #     j = i
        #     run = 0
        #     while j < len(questions):
        #         q = questions[j]
        #         run += q[0]
        #         j += q[1] + 1
        #         skip.add(j)
        #     ans.add(run)
        # return max(ans)

        if len(questions) == 1:
            return questions[0]

        my_q = []
        for q in questions[1:]:
            pass
        return max([self.mostPoints(questions[i:]) for i in range(0, len(questions))])


if __name__ == "__main__":
    sol = Solution()
    tests = [[[3, 2], [4, 3], [4, 4], [2, 5]],
             [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]]
    for te in tests:
        res = sol.mostPoints(te)
        print(f"{te}: --> {res}")


# https://leetcode.com/problems/solving-questions-with-brainpower/submissions/1330117296/