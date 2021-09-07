class Solution{		// 8ms
	public List<List<Integer>> combine(int n, int k){
		List<List<Integer>> ret = new ArrayList<>();

		if(n < k || k == 0) return ret;

		ret = combine(n - 1, k - 1);
		if(ret.isEmpty()) ret.add(new ArrayList<Integer>());
		for(List<Integer> list : ret) list.add(n);

		ret.addAll(combine(n - 1. k));

		return ret;
	}
}