class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;

        char[] arr = String.valueOf(x).toCharArray();

        for(int i = 0; i < arr.length / 2; i++){
            if(arr[i] != arr[arr.length - 1 - i]) return false;
        }
        return true;
    }
}