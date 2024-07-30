class Solution(object):
    def minimumDeletions(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        b_count = 0

        for c in s:
            if c == 'a':
                ret = min(b_count, ret + 1)
            else:
                b_count += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "b",
        "aababbab",
        "bbaaaaabb",
        "aabbbbaabababbbbaaaaaabbababaaabaabaabbbabbbbabbabbababaabaababbbbaaaaabbabbabaaaabbbabaaaabbaaabbbaabbaaaaabaa"
    ]
    for te in tests:
        res = sol.minimumDeletions(te)
        print(f"{te}: --> {res}")
