import java.lang.Math;

class Solution {        // 26ms
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int[][] dynArr = new int[arr.length][arr.length];
        for(int i = 0; i < arr.length; i++){
            for(int j = i; j < arr.length; j++){
                dynArr[i][j] = Math.abs(arr[i] - arr[j]);
            }
        }

        int ret = 0;
        for(int i = 0; i < arr.length - 2; i++){
            for(int j = i + 1; j < arr.length - 1; j++){
                for(int k = j + 1; k < arr.length; k++){
                    if(dynArr[i][j] <= a && dynArr[j][k] <= b && dynArr[i][k] <= c)
                        ret++;
                }
            }
        }
        return ret;
    }
}