# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        last, n = head, 1
        while last.next:
            n += 1
            last = last.next
        k = k % n
        last.next = head
        mid = head
        for _ in range(n - k - 1):
            mid = mid.next
        first = mid.next
        mid.next = None
        return first

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(0, ListNode(1, ListNode(2)))
    print(sol.rotateRight(head, 4))