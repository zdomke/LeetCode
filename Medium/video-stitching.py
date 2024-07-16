class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        prev, cur, count = -1, 0, 0
        for l, r in sorted(clips):
            if l > cur or cur >= time: break
            if prev < l <= cur: prev, count = cur, count + 1
            cur = max(cur, r)
        return count if cur >= time else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))