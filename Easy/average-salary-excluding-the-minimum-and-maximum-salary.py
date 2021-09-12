class Solution:     # 37ms
    def average(self, salary: List[int]) -> float:
        runSum = 0
        runMax = salary[0]
        runMin = runMax
        for i in range(len(salary)):
            runSum += salary[i]
            runMax = max(salary[i], runMax)
            runMin = min(salary[i], runMin)
        return (runSum - runMax - runMin) / (len(salary) - 2)