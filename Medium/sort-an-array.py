class Solution(object):
    def sortArray(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(arr):
            if len(arr) == 1:
                return

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            merge(left)
            merge(right)

            ind_l = ind_r = ind_a = 0

            while ind_l < len(left) and ind_r < len(right):
                if left[ind_l] < right[ind_r]:
                    arr[ind_a] = left[ind_l]
                    ind_l += 1
                else:
                    arr[ind_a] = right[ind_r]
                    ind_r += 1
                ind_a += 1

            if ind_l < len(left):
                arr[ind_a:] = left[ind_l:]

            if ind_r < len(right):
                arr[ind_a:] = right[ind_r:]

        merge(nums)
        return nums


if __name__ == "__main__":
    sol = Solution()
    tests = [([5, 2, 3, 1],),
             ([5, 1, 1, 2, 0, 0],)]
    for te in tests:
        res = sol.sortArray(*te)
        print(f"{te}: --> {res}")
