class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        k -= 1
        small = nums[-1]
        for i in range(len(nums) - k):
            small = min(small, nums[i + k] - nums[i])
        return small