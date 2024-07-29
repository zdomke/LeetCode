class Solution(object):
    def maximumOddBinaryNumber(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        o_count = s.count('1')
        z_count = len(s) - o_count

        return ('1' * (o_count - 1)) + ('0' * z_count) + '1'

    def diff_solution(self, s: str):
        s = sorted(s)
        o_count = s.count('1') - 1
        s = s[-o_count:] + s[:-o_count]
        return ''.join(s)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("010"),
        ("0101"),
    ]
    for te in tests:
        res = sol.maximumOddBinaryNumber(te)
        print(f"{te}: --> {res}")
