class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;
        
        int y = 0;
        int copy = x;
        
        while (copy > 0){
            y = (y * 10) + (copy % 10);
            copy /= 10;
        }
        
        return x == y;
    }
}