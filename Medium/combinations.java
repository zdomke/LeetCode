import java.lang.Math;

class Solution{		// 24ms
	public List<List<Integer>> combine(int n, int k){
		double len = Math.pow(2, n);
		List<List<Integer>> ret = new List<>();
		
		for(int i = 1; i <= len; i++){
			if(Integer.bitCount(i) != k) continue;
			String bits = Integer.toBinaryString(i);
			List<Integer> temp = new ArrayList<>();
			for(int j = 0; j < n; j++){
				if(bits.charAt(bits.length() - j) == '1'){
					temp.add(j + 1);
				}
			}
			ret.add(temp);
		}
		return ret;
	}
}