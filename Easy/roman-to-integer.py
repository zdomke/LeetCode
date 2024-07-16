class Solution(object):

    def romanToInt(self, s: str):
        conv = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        ret = 0
        prev = 0

        for c in s[::-1]:
            if conv[c] >= prev:
                ret += conv[c]
            else:
                ret -= conv[c]
            prev = conv[c]
        return ret


if __name__ == "__main__":
    sol = Solution()
    strs = ["III", "LVIII", "MCMXCIV"]
    for s in strs:
        print(f"{s} --> {sol.romanToInt(s)}")
