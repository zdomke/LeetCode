class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = ['']
        for c in s:
            if c == '(':
                st.append('')
            elif c == ')':
                temp = st.pop()[::-1]
                st[-1] += temp
            else:
                st[-1] += c
        return st.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseParentheses("(abcd)"))
    print(sol.reverseParentheses("(u(love)i)"))