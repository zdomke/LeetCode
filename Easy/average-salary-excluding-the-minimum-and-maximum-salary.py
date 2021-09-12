class Solution:     # 32ms
    def average(self, salary: List[int]) -> float:
        runSum = 0
        extreme = [salary[0]] * 2
        for i in range(len(salary)):
            runSum += salary[i]
            extreme[0] = max(salary[i], extreme[0])
            extreme[1] = min(salary[i], extreme[1])
        return (runSum - extreme[0] - extreme[1]) / (len(salary) - 2)