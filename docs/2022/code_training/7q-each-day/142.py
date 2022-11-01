# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = fast_ptr = head

        # If a pointer reaches None, then the list has an exit, so no loops.
        while fast_ptr != None \
              and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            # If fast_ptr catches slow_ptr from behind, then there must be a loop.
            if slow_ptr == fast_ptr:
                break

        # if while loop ended because of end-of-list, then there is no loop.
        if fast_ptr == None or fast_ptr.next == None:
            return None

        # Otherwise, there is a loop!! Now find the entrance to it.
        # There is no need to check for None because we already know that
        # there is no end in this list.
        # This will not be an infinite loop because of math! the pointers
        # are guaranteed to meet at the entrance.
        slow_ptr2 = head
        while slow_ptr != slow_ptr2:
            slow_ptr = slow_ptr.next
            slow_ptr2 = slow_ptr2.next

        return slow_ptr
