# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], \
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if one list is not defined, return the other
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        # both lists exists and have at least one element.
        # lead_f (front) and lead_r (rear) are two pointers
        # the beginning of the list with smaller initial value.
        # front is normally closer to the tail.
        # other_f and other_r are two pointers to the beginning
        # of the other list.
        # result_head is what we will return.
        if list1.val < list2.val:
            lead_r,other_r = (list1,list2)
        else:
            lead_r,other_r = (list2,list1)
        result_head = lead_r
        lead_f,other_f = lead_r.next,other_r.next;

        '''
        1  2  4
        1  3  4
        '''
        # traverse lists, identifying where to cut lead to
        # insert parts of other.
        while lead_f != None and other_f != None:

            # move the pair [lead_r,lead_f] forward for as long as
            # lead_f is smaller than other_r.
            while lead_f != None and lead_f.val < other_r.val:
                lead_r = lead_f
                lead_f = lead_f.next
            
            # we found the cutting point in lead: right between
            # lead_r and lead_f.
            # Now we find how long is the segment in 'other'
            # that will be injected into lead.

            # if lead_f is None, then lead_r is the last
            # element of lead, therefore, we just attach
            # everything from other at the end of lead; and
            # we are done.
            if lead_f == None:    
                lead_r.next = other_r
                return result_head
                
            # try to expand the segment in other by moving other_f
            # forward for as long as other_f can go before lead_f.
            # other_m (middle) keeps track of the node before other_f
            other_m = other_r
            while other_f != None and other_f.val <= lead_f.val:
                other_m = other_f
                other_f = other_f.next
                
            # other_m is now the last element in the segment
            # of other that goes between lead_r and lead_f.
            # Now patch the pointers.
            # 1  2\         /6  7
            #      \3  4  5/
            lead_r.next = other_r
            other_m.next = lead_f
            
            # if other_f is null, then we are done.
            # but if lead_f is null AND other_f is still something,
            # we attach the remainder of other to the end of lead
            # before exiting.
            if other_f == None:
                break
            if lead_f == None:
                lead_f.next = other_f
                break

            # if none is null, then there is more work to do.
            lead_r,other_r = lead_f,other_f
            lead_f,other_f = lead_f.next,other_f.next
        return result_head
