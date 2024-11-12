class Solution(object):
    def maximumBeauty(self, items: list, queries: list):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort()
        beauty = [items[0][1]] * len(items)

        for i in range(1, len(items)):
            beauty[i] = max(beauty[i - 1], items[i][1])

        def bs(t):
            ans = 0
            s = 0
            e = len(items) - 1

            while s <= e:
                m = (s + e) // 2
                if items[m][0] <= t:
                    ans = beauty[m]
                    s = m + 1
                else:
                    e = m - 1
            return ans

        ret = [bs(q) for q in queries]

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [1, 2], [1, 3], [1, 4]], [1]),
        ([[10, 1000]], [5]),
    ]
    for te in tests:
        res = sol.maximumBeauty(*te)
        print(f"{te}: --> {res}")
