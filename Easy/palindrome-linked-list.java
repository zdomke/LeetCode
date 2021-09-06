class Solution{		// 11ms
	public boolean isPalindrom(ListNode head){
		ArrayDeque<Integer> arr = new ArrayDeque<>();
		while(head != null){
			arr.push(head.val);
            head = head.next;
        }
		while((arr.size() != 0) && (arr.size() != 1)){
			if(arr.pollFirst() != arr.pollLast())
				return false;
		}
		return true;
	}
}