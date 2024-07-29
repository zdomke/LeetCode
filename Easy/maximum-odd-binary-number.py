class Solution(object):
    def maximumOddBinaryNumber(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        o_count = s.count('1')
        z_count = len(s) - o_count

        return ('1' * (o_count - 1)) + ('0' * z_count) + '1'


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("010"),
        ("0101"),
    ]
    for te in tests:
        res = sol.maximumOddBinaryNumber(te)
        print(f"{te}: --> {res}")
