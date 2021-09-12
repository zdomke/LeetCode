class Solution:     # 1208ms
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev = 0
        for i in range(k):
            prev += nums[i]
        ret = prev
        for i in range(len(nums) - k):
            prev = prev - nums[i] + nums[i + k]
            ret = max(prev, ret)
        return ret / k