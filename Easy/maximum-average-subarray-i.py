class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        dp = []
        avg = 0
        for i in range(k):
            avg = ((avg * i) + nums[i]) / (i + 1)
        dp.append(avg)
        print(dp[0])
        for i in range(len(nums) - k):
            dp.append(((dp[i] * k) - nums[i] + nums[i + k]) / k)
            print(dp[-1])
        dp.sort()
        return dp[-1]