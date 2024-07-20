class Solution(object):
    def wordPattern(self, pattern: str, s: str):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        di_ch = {}
        di_wo = {}
        spl = s.split()
        if len(spl) != len(pattern):
            return False

        for ch, wo in zip(pattern, spl):
            if ch not in di_ch or wo not in di_wo:
                if ch not in di_ch and wo not in di_wo:
                    di_ch[ch] = wo
                    di_wo[wo] = ch
                    continue
                return False
            elif di_ch[ch] != wo or di_wo[wo] != ch:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [("abba", "dog cat cat dog"),
             ("abba", "dog cat cat fish"),
             ("aaaa", "dog cat cat dog"),
             ("abba", "dog dog dog dog")]
    for te in tests:
        print(f"{te} --> {sol.wordPattern(*te)}")
