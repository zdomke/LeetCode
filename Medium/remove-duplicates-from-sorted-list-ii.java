class Solution{			// 0ms
	public ListNode deleteDuplicates(ListNode head){
		ListNode start = new ListNode(-101, head);
		ListNode prev = start;
		int dup = -101;

		while(head != null){
			if(head.val != dup &&
               head.val != prev.val &&
               (head.next == null || head.val != head.next.val)){
                prev.next = head;
                prev = head;
			} else {
				dup = head.val;
			}
			head = head.next;
		}
		prev.next = null;

		return start.next;
	}
}