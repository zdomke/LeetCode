class Solution:
    def minOperations(self, s:str) -> int:
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations("10"))
    print(sol.minOperations("0100"))
    print(sol.minOperations("110010"))