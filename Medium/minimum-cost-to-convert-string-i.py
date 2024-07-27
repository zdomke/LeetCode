class Solution(object):
    def minimumCost(self, source: str, target: str, original: list, changed: list, cost: list):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        indices = {}
        count = 0
        for c in original + changed:
            if c not in indices:
                indices[c] = count
                count += 1
        n = len(indices)

        matrix = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0

        for i in range(len(original)):
            ind_ori = indices[original[i]]
            ind_cha = indices[changed[i]]

            matrix[ind_ori][ind_cha] = min(matrix[ind_ori][ind_cha], cost[i])

        for v in range(n):
            for o in range(n):
                for c in range(n):
                    matrix[o][c] = min(matrix[o][c],
                                       matrix[o][v] + matrix[v][c])

        ret = 0
        for s, t in zip(source, target):
            try:
                ind_sou = indices[s]
                ind_tar = indices[t]

                val = matrix[ind_sou][ind_tar]
                if val == float("inf"):
                    return -1
                ret += val
            except KeyError:
                return -1

        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]),
        ("aaaa", "bbbb", ["a","c"], ["c","b"], [1, 2]),
        ("abcd", "abce", ["a"], ["e"], [1000]),
    ]
    for te in tests:
        res = sol.minimumCost(*te)
        print(f"{te}: --> {res}")
