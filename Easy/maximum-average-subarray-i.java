import java.lang.Math;

class Solution {        // 7ms
    public double findMaxAverage(int[] nums, int k) {
        double prev = 0;
        for(int i = 0; i < k; i++){
            prev += nums[i];
        }
        double ret = prev / k;
        for(int i = 0; i < nums.length - k; i++){
            prev += nums[i + k] - nums[i];
            ret = Math.max(prev / k, ret);
        }
        return ret;
    }
}