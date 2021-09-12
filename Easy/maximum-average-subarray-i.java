class Solution {        // 4ms
    public double findMaxAverage(int[] nums, int k) {
        double prev = 0;
        for(int i = 0; i < k; i++){
            prev += nums[i];
        }
        double ret = prev;
        for(int i = 0; i < nums.length - k; i++){
            prev += nums[i + k] - nums[i];
            ret = Math.max(prev, ret);
        }
        return ret / k;
    }
}