class Solution{		// 1ms
	public int reachNumber(int target){
		target = Math.abs(target);
		int val = 0;
		int k = 1;
		while(val < target){
			val += k++;
		}
		k--;
		if((val - target) % 2 == 0)
			return k;
		if((val + (k + 1) - target) % 2 == 0)
			return (k + 1);
		return (k + 2);
	}
}