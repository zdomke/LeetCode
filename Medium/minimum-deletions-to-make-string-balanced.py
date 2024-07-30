class Solution(object):
    def minimumDeletions(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        a_count = s.count('a')
        b_count = 0

        ret = a_count
        for c in s:
            if c == 'b':
                b_count += 1
            else:
                a_count -= 1

            ret = min(ret, a_count + b_count)

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
