class Solution(object):
    def findTheCity(self, n: int, edges: list, distanceThreshold: int):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        cities = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            cities[i][i] = 0

        for i, j, k in edges:
            cities[i][j] = k
            cities[j][i] = k

        for v in range(n):
            for s in range(n):
                for d in range(n):
                    cities[s][d] = min(cities[s][d],
                                       cities[s][v] + cities[v][d])

        ret = -1
        min_cities = float("inf")
        for i in range(n):
            count = 0
            for j in range(n):
                count += i != j and cities[i][j] <= distanceThreshold

            if count <= min_cities:
                min_cities = count
                ret = i

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2),
    ]
    for te in tests:
        res = sol.findTheCity(*te)
        print(f"{te}: --> {res}")
