class Solution:     # 317ms
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False 
        
        i = 1
        while i < len(arr) - 1 and arr[i - 1] < arr[i]:
            i += 1
        while i < len(arr) and arr[i - 1] > arr[i]:
            i += 1
        return i == len(arr)