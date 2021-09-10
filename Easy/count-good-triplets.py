class Solution:     # 533ms
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        dynArr = []
        for i in range(len(arr) - 1):
            temp = [0] * len(arr)
            for j in range(i, len(arr)):
                temp[j] = abs(arr[i] - arr[j])
            dynArr.append(temp)
                
        ret = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if dynArr[i][j] <= a and dynArr[j][k] <= b and dynArr[i][k] <= c:
                            ret += 1
        return ret