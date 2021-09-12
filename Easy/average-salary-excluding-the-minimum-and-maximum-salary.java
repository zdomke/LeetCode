class Solution {        // 0ms
    public double average(int[] salary) {
        double sum = 0;
        int min = salary[0];
        int max = salary[0];
        for(int x : salary){
            sum += x;
            min = Math.min(x, min);
            max = Math.max(x, max);
        }
        return (sum - min - max) / (salary.length - 2);
    }
}