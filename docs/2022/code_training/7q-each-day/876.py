# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        slow_ptr = fast_ptr = head
        odd_loop = True
        while fast_ptr.next != None:
            fast_ptr = fast_ptr.next
            # move slow_ptr only in odd loops
            if odd_loop:
                slow_ptr = slow_ptr.next
            odd_loop = not odd_loop
        return slow_ptr
    
