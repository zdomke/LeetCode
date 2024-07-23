class Solution(object):
    def asteroidsDestroyed(self, mass: int, asteroids: list):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [(10, [3, 9, 19, 5, 21]),
             (5, [4, 9, 23, 4])]
    for te in tests:
        res = sol.asteroidsDestroyed(*te)
        print(f"{te}: --> {res}")
