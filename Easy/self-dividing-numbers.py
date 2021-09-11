class Solution:     # 70ms
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right + 1):
            tempBool = True
            tempStr = str(i)
            for x in tempStr:
                if x == '0':
                    tempBool = False
                    break
                tempBool = tempBool and (i % int(x) == 0)
            if tempBool:
                ret.append(i)
        return ret