class Solution:     # 35ms
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ret = []
        for w in s:
            ret.append(w[::-1])
        return " ".join(ret)