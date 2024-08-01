class Solution(object):
    def countSeniors(self, details: list):
        """
        :type details: List[str]
        :rtype: int
        """
        ret = 0
        for p in details:
            ret += int(p[11:13]) > 60

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ["7868190130M7522", "5303914400F9211", "9273338290F4010"],
        ["1313579440F2036", "2921522980M5644"],
    ]
    for te in tests:
        res = sol.countSeniors(te)
        print(f"{te}: --> {res}")
