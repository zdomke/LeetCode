class Solution{		// 22ms
	public boolean isPalindrom(ListNode head){
		Stack<Integer> st = new Stack<>();
		ListNode curr = head;
		while(curr != null){
			st.push(curr.val);
            curr = curr.next;
        }
		curr = head;
		while(!st.empty()){
			if(st.pop() != curr.val)
				return false;
			curr = curr.next;
		}
		return true;
	}
}