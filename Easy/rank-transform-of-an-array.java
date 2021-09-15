class Solution{			// 75ms
	public int[] arrayRankTransform(int[] arr){
		HashMap<Integer, Integer> hm = new HashMap<>();
		int[] copy = arr.clone();
		Arrays.sort(copy);
		for(int x : copy){
			if(!hm.containsKey(x)){
				hm.put(x, hm.size() + 1);
			}
		}
		for(int i = 0; i < arr.length; i++){
			copy[i] = hm.get(arr[i]);
		}
		return copy;
	}
}