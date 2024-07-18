class Solution(object):
    def longestCommonPrefix(self, strs: list):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        s0 = ""
        max_len = min([len(s) for s in strs])
        for i in range(max_len):
            s0 = strs[0][:i+1]
            for s in strs[1:]:
                if s.startswith(s0):
                    continue
                return s0[:-1]
        return s0


if __name__ == "__main__":
    sol = Solution()
    lists = [["flower", "flow", "flight"],
             ["dog", "racecar", "car"],
             ["", ""],
             ["", "b"],
             ["ab", "a"],
             ["abab", "aba", ""]]
    for l in lists:
        print(f"{l} --> {sol.longestCommonPrefix(l)}")
