class Solution {
    public boolean canJump(int[] nums) {
        int ind = 0;
        int val = nums[0];
        int last = nums.length - 1;
        int[] temp;

        while((ind + val != ind) && (ind + val < last)){
            ind++;
            temp = Arrays.copyOfRange(nums, ind, ind + val);
            val = 0;
            int newInd = 0;
            for(int i = 0; i < temp.length; i++){
                if(val <= i + temp[i]){
                    newInd = i;
                    val = temp[i];
                }
            }
            ind += newInd;
        }
        return (ind + val >= last);
    }
}

class Solution {
    public boolean canJump(int[] nums) {
        int next;
        boolean[] arr = new boolean[nums.length];

        for(int i = (arr.length - 1); i >= 0; i--){
            next = nums[i] + i;
            arr[i] = next >= (nums.length - 1);
            for(int j = (i + 1); j <= next; j++){
                if(arr[i])
                    break;
                arr[i] |= arr[j];
            }
        }
        return arr[0];
    }
}

class Solution{
    public boolean canJump(int[] nums){
        int ind = nums.length - 1;
        for(int i = ind; i >= 0; i--){
            if(i + nums[i] >= ind)
                ind = i;
        }
        return (ind == 0);
    }
}

class Solution{
    public boolean canJump(int[] nums){
        int run = 0;
        for(int i = 0; i < (nums.length - 1); i++){
            if(run < i)
                return false;
            run = Math.max(run, i + nums[i]);
        }
        return true;
    }
}