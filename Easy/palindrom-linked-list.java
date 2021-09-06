class Solution{		// 23ms
	public boolean isPalindrom(ListNode head){
		ArrayList arr = new ArrayList<Integer>();
		while(head != null){
			arr.add(head.val);
			head = head.next;
		}
		int len = arr.size();
		for(int i = 0; i < (len / 2); i++){
			if(arr.get(i) != (arr.get(len - 1 - i)))
				return false;
		}
		return true;
	}
}