class Solution:         # 48ms
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right + 1):
            tempBool = True
            tempStr = str(i)
            for x in tempStr:
                if x == '0' or (i % int(x) != 0):
                    tempBool = False
                    break
            if tempBool:
                ret.append(i)
        return ret