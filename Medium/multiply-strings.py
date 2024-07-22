class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tens = 1
        prods = []
        num1 = [int(n) for n in num1]
        num2 = [int(n) for n in num2]

        for i in num1[::-1]:
            tens2 = 1
            for j in num2[::-1]:
                prods.append(i * j * tens * tens2)
                tens2 *= 10
            tens *= 10
        return str(sum(prods))

    def best_solution(self, num1, num2):
        return str(eval(num1 + "*" + num2))


if __name__ == "__main__":
    sol = Solution()
    tests = [("2", "3"),
             ("123", "456")]
    for te in tests:
        res = sol.best_solution(*te)
        print(f"{te}: --> {res}")
