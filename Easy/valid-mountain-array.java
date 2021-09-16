class Solution {        // 1ms
    public boolean validMountainArray(int[] arr) {
        int n = arr.length;
        int i = 0;
        
        for(; i + 1 < n && arr[i] < arr[i + 1]; i++);
        if(i == 0 || i + 1 == n) return false;
        for(; i + 1 < n && arr[i] > arr[i + 1]; i++);
        return i == n - 1;
    }
}