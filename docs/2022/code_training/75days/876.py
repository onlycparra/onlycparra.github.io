# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tip = mid = head
        count = 0
        while tip.next:
            tip = tip.next
            if count % 2 == 0:
                mid = mid.next
            count += 1
        return mid
