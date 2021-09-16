class Solution:     # 196ms
    def validMountainArray(self, arr: List[int]) -> bool:
        ln = len(arr)
        i = 0
        while(i < ln - 1 and arr[i] < arr[i + 1]):
            i += 1
        if(i == 0 or i == ln - 1):
            return False
        while(i < ln - 1 and arr[i] > arr[i + 1]):
            i += 1
        return i == ln - 1