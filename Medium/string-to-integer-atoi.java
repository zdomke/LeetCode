class Solution{
	public int myAtoi(String s){
		s = s.trim();
        if(s.length() == 0){
            return 0;
        }
        
		boolean neg = false;
		long run = 0;
        int i = 0;
        char curr = s.charAt(i);
    
        if(curr == '+' || curr == '-'){
            neg = curr == '-';
            i++;
        }
		for(; i < s.length(); i++){
            curr = s.charAt(i);
            if(Character.isDigit(curr)){
				run *= 10;
				run += Character.getNumericValue(curr);
                if((run < 0) || (run > Integer.MAX_VALUE)){
                    return neg ? Integer.MIN_VALUE : Integer.MAX_VALUE;
                }
			} else {
				break;
			}
		}
        run *= neg ? -1 : 1;

		return (int)run;
	}
}