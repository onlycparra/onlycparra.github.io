# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        new_head = head
        orig_head = head.next # maybe None
        new_head.next = None # the ending of the new list
        # None <--nh    h--> ...--> None
        while orig_head != None:
            temp_head = orig_head
            orig_head = orig_head.next # maybe None
            # None <--nh   th--> h--> ...--> None
            
            temp_head.next = new_head
            # None <--nh <--th    h--> ...--> None

            new_head = temp_head
            # None <--?? <--nh    h--> ...--> None
            
        return new_head
