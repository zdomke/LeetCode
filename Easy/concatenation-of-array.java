class Solution {        // 0ms
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n * 2];
        
        for(int i = 0; i < n; i++){
            ret[i + n] = ret[i] = nums[i];
        }
        return ret;
    }
}