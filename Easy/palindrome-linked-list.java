class Solution{		// 5ms
	public boolean isPalindrome(ListNode head){
		ListNode slow = head;
		ListNode fast = head;
		while((fast != null) && (fast.next != null)){
			slow = slow.next;
			fast = fast.next.next;
		}
		if(fast != null) slow = slow.next;

		slow = reverse(slow);
		fast = head;

		while(slow != null){
			if(slow.val != fast.val) return false;
			slow = slow.next;
			fast = fast.next;
		}
		return true;
	}

	private ListNode reverse(ListNode head){
		ListNode prev = null;
		while(head != null){
			ListNode next = head.next;
			head.next = prev;
			prev = head;
			head = next;
		}
		return prev;
	}
}

/*
Pros:
	Runs very quickly
Cons:
	Uses a lot of space
	Modifies original LinkedList
*/