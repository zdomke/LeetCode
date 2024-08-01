class Solution(object):
    def minimumLength(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        elif s[0] != s[-1]:
            return len(s)

        s = s.lstrip(s[0]).rstrip(s[0])
        return self.minimumLength(s)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "ca",
        "cabaabac",
        "aabccabba",
    ]
    for te in tests:
        res = sol.minimumLength(te)
        print(f"{te}: --> {res}")
