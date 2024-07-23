class Solution(object):
    def strStr(self, haystack: str, needle: str):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            ind = haystack.index(needle)
        except ValueError:
            ind = -1
        return ind


if __name__ == "__main__":
    sol = Solution()
    tests = [("sadbutsad", "sad"),
             ("leetcode", "leeto")]
    for te in tests:
        res = sol.strStr(*te)
        print(f"{te}: --> {res}")
