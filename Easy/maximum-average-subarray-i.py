class Solution:     # 1409ms
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev = 0
        for i in range(k):
            prev += nums[i]
        ret = prev / k
        for i in range(len(nums) - k):
            prev = prev - nums[i] + nums[i + k]
            ret = max(prev / k, ret)
        return ret