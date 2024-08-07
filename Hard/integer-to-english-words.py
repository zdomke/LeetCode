class Solution(object):
    def numberToWords(self, num: int):
        """
        :type num: int
        :rtype: str
        """
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                ind = (n // 10) - 2
                return [tens[ind]] + words(n % 10)
            if n < 1000:
                ind = (n // 100) - 1
                return [to19[ind]] + ["Hundred"] + words(n % 100)

            for p, w in enumerate(("Thousand", "Million", "Billion"), 1):
                if n < (1000 ** (p + 1)):
                    return words(n // (1000 ** p)) + [w] + words(n % (1000 ** p))

        return ' '.join(words(num)) if num else "Zero"


if __name__ == "__main__":
    sol = Solution()
    tests = [
        123,
        12345,
        1234567,
        0
    ]
    for te in tests:
        res = sol.numberToWords(te)
        print(f"{te}: --> {res}")
