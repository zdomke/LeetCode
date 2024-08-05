class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dist = 0
        for s in arr:
            if arr.count(s) == 1:
                dist += 1
                if dist == k:
                    return s
        return ""


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["d", "b", "c", "b", "c", "a"], 2),
        (["aaa", "aa", "a"], 1),
        (["a", "b", "a"], 3),
    ]
    for te in tests:
        res = sol.kthDistinct(*te)
        print(f"{te}: --> {res}")
