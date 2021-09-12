class Solution {        // 0ms
    public double average(int[] salary) {
        double[] run = {0, salary[0], salary[0]};
        for(int i = 0; i < salary.length; i++){
            run[0] += salary[i];
            run[1] = Math.min(run[1], salary[i]);
            run[2] = Math.max(run[2], salary[i]);
        }
        return (run[0] - run[1] - run[2]) / (salary.length - 2);
    }
}