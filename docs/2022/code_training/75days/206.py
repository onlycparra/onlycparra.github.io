# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = None
        while head.next: #to check
            tmp_nxt = head.next
            head.next = tail
            tail = head
            head = tmp_nxt
        head.next = tail
        return head
        
