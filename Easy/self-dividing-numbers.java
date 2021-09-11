class Solution{		// 14ms
    public List<Integer> selfDividingNumbers(int left, int right){
    	List<Integer> ret = new ArrayList<>();

    	for(int i = left; i <= right; i++){
    		boolean bool = true;
    		char[] arr = String.valueOf(i).toCharArray();
    		for(int j = 0; j < arr.length; j++){
    			if((arr[j] == '0') || (i % Character.getNumericValue(arr[j]) != 0)){
    				bool = false;
    				break;
    			}
    		}
    		if(bool)
	    		ret.add(i);
    	}
    	return ret;
    }
}