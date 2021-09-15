class Solution{			// 24ms
	public int[] arrayRankTransform(int[] arr){
		HashMap<Integer, Integer> hm = new HashMap<>();
		int[] a = arr.clone();
		Arrays.sort(copy);
		for(int x : a){
			hm.putIfAbsent(x, hm.size() + 1);
		}
		for(int i = 0; i < arr.length; i++){
			a[i] = hm.get(arr[i]);
		}
		return a;
	}
}