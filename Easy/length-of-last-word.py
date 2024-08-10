class Solution(object):
    def lengthOfLastWord(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])


if __name__ == "__main__":
    sol = Solution()
    tests = ["Hello World",
             "   fly me   to   the moon  ",
             "luffy is still joyboy"]
    for te in tests:
        res = sol.lengthOfLastWord(te)
        print(f"{te}: --> {res}")
