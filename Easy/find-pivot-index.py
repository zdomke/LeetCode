class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pivot = 0
        left = 0
        right = sum(nums) - nums[0]
        while left < right and pivot < len(nums) - 1:
            left += nums[pivot]
            pivot += 1
            right -= nums[pivot]
        return -1 if left != right else pivot