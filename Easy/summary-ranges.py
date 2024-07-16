class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ret = []
        start = 0
        end = 0
        while(end < (len(nums) - 1)):
            if nums[end] + 1 != nums[end + 1]:
                ret.append(str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}")
                start = end + 1
            end += 1
        ret.append(str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}")
        return ret

def main():
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    print(sol.summaryRanges(nums))


if __name__ == "__main__":
    main()