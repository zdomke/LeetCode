class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(date[:4])
        mo = int(date[5:7])
        day = int(date[8:])
        ret = sum(days[:mo - 1]) + day
        if year % 4 == 0 and mo > 2:
            ret += 1
        return ret