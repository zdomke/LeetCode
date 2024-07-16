class Solution:
    def find132pattern(self, nums:list[int]) -> bool:
        st = []
        s3 = min(nums)
        for n in nums[::-1]:
            if n < s3:
                return True
            while st and st[-1] < n:
                s3 = st.pop()
            st.append(n)
        return False