class Solution{
	public int maxWidthRamp(int[] nums){
		int[] ramps = new int[nums.length];
		Stack<Integer> st = new Stack<>();

		for(int i = nums.length - 1; i >= 0; i--){
			while(!st.empty() && (nums[st.peek()] < nums[i]))
				st.pop();
			ramps[i] = st.empty() ? 0 : (st.peek() - i + ramps[st.peek()]);
			st.push(i);
		}
		Arrays.sort(ramps);
		return ramps[ramps.length - 1];
	}
}


/*
Does not work properly.
It stops iterating through the stack at the first event of a larger value in nums.
*/