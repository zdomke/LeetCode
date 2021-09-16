class Solution {        // 1ms
    public boolean validMountainArray(int[] arr) {
        int n = arr.length;
        if(n < 3) return false;
        int first = 0;
        int last = n - 1;
        
        while(first < last){
            if(arr[first] < arr[first + 1]){
                first++;
            } else if(arr[last] < arr[last - 1]){
                last--;
            } else {
                break;
            }
        }
        return (first != 0) && (last != n - 1) && (first == last);
    }
}