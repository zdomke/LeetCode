class Solution:     # 1521ms
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev = 0
        for i in range(k):
            prev = ((prev * i) + nums[i]) / (i + 1)
        ret = prev
        for i in range(len(nums) - k):
            prev = ((prev * k) - nums[i] + nums[i + k]) / k
            ret = max(prev, ret)
        return ret