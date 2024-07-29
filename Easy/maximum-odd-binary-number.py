class Solution(object):
    def maximumOddBinaryNumber(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        count0 = s.count('0')
        count1 = s.count('1') - 1
        ret = '1' * count1 + '0' * count0 + '1'
        return ret

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
