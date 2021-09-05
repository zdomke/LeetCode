class Solution{			// 6ms
	public int maxWidthRamp(int[] nums){
		Stack<Integer> st = new Stack<>();
		int ramp = 0;
		int len = nums.length;
		for(int i = 0; i < len; i++){
			if(st.empty() || (nums[st.peek()] > nums[i]))
				st.add(i);
		}
		for(int i = len - 1; i > ramp; i--){
			while(!st.empty() && (nums[st.peek()] <= nums[i]))
				ramp = Math.max(ramp, i - st.pop());
		}
		return ramp;
	}
}