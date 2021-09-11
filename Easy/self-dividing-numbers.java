class Solution{		// 5ms
    public List<Integer> selfDividingNumbers(int left, int right){
    	boolean[] digits = new boolean[10];
    	List<Integer> ret = new ArrayList<>();

    	for(int i = left; i <= right; i++){
            for(int j = 0; j < 10; j++)
                digits[j] = false;
	    	int j = i;
	    	while(j > 0){
	    		digits[j % 10] = true;
	    		j /= 10;
	    	}
    		boolean bool = true;
	    	if(!digits[0]){
	    		for(j = 1; j < 10; j++){
	    			if(digits[j] && i % j != 0){
	    				bool = false;
	    				break;
	    			}
	    		}
	    	} else {
	    		bool = false;
	    	}
    		if(bool)
	    		ret.add(i);
    	}
    	return ret;
    }
}