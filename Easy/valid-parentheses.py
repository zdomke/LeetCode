class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        st = []
        for c in s:
            if c in d.values():
                st.append(c)
            elif st and st[-1] == d[c]:
                st.pop(-1)
            else:
                return False
        return not st