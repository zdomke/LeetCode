class Solution(object):
    def minimumLength(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        char = s[0]
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break

            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1

            char = s[right]

        return right - left + 1


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
