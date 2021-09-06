class Solution{		// 20ms
	private ListNode curr;
	public boolean isPalindrome(ListNode head){
		curr = head;
		return helper(head);
	}

	private boolean helper(ListNode node){
		if(node == null) return true;

		boolean sub = helper(node.next) && (node.val == curr.val);
		curr = curr.next;
		return sub;
	}
}