class Solution{			// 0ms
	public boolean hasAlternatingBits(int n){
		int lastBit = n % 2;
		int currBit;
		n /= 2;
		while(n > 0){
			currBit = n % 2;
			n /= 2;
			if(currBit == lastBit) return false;
			lastBit = currBit;
		}
		return true;
	}
}