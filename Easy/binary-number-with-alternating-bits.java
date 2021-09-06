class Solution{			// 9ms
	public boolean hasAlternatingBits(int n){
		String run = "";
		while(n > 0){
			run += (n % 2);
			n /= 2;
		}
		for(int i = 1; i < run.length(); i++){
			if(run.charAt(i) == run.charAt(i - 1))
				return false;
		}
		return true;
	}
}