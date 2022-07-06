# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        # let them run!
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # if the list has no loops
        if fast == None or fast.next == None:
            return None

        # meet each other at the entrance of the loop
        p1 = head # one start from the head,
        p2 = slow # and the other from the meeting point.
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
    
