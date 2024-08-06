class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        my_map = {c: word.count(c) for c in set(word)}
        sort_map = sorted(my_map.items(), key=(lambda it: it[1]), reverse=True)

        ret = 0
        for i, item in enumerate(sort_map):
            ret += item[1] * ((i // 8) + 1)
        return ret


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcde"),
        ("xyzxyzxyzxyz"),
        ("aabbccddeeffgghhiiiiii")
    ]
    for te in tests:
        res = sol.minimumPushes(te)
        print(f"{te}: --> {res}")
