class Solution {        // 0ms
    public int minTimeToVisitAllPoints(int[][] points) {
        int t = 0;
        int[] curr = points[0];
        for(int[] point : points){
            t+= Math.max(Math.abs(point[0] - curr[0]), Math.abs(point[1] - curr[1]));
            curr = point;
        }
        return t;
    }
}