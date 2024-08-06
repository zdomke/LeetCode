class Solution(object):
    def customSortString(self, order: str, s: str):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        def sort(c):
            try:
                return order.index(c)
            except ValueError:
                return 0

        return "".join(sorted(s, key=sort))

    def second_sol(self, order, s):
        key = {order[i]: i for i in range(len(order))}

        return "".join(sorted(s, key=lambda c: key.get(c, -1)))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("cba", "abcd"),
        ("bcafg", "abcd"),
    ]
    for te in tests:
        res = sol.customSortString(*te)
        print(f"{te}: --> {res}")
