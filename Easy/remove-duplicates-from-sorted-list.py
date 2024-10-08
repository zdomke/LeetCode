# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node != None and node.next != None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head