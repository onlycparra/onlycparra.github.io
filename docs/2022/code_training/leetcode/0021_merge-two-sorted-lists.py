# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], \
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        '''if one list is not defined, return the other'''
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        '''Rear pointers pointing to:
        - lead: the list with the smallest first element
        - other: the... other list :)'''
        if list1.val < list2.val:
            lead_r,other_r = (list1,list2)
        else:
            lead_r,other_r = (list2,list1)
            
        '''front pointers that will be ahead of {lead,other}_r'''
        lead_f,other_f = lead_r.next,other_r.next;

        '''pointer to return at the end of the function'''
        result_head = lead_r

        '''    lr  lf
        lead : 1   2   6   8   9
        other: 3   4   5   7
               or  of
        '''
        
        '''Find the cutting point in 'lead', and the segment from 'other'
        to insert it in the cut.'''
        while lead_r != None and other_r != None:

            # move the pair [lead_r,lead_f] forward for as long as
            # lead_f is smaller than other_r.
            while lead_f != None and lead_f.val < other_r.val:
                lead_r = lead_f
                lead_f = lead_f.next
            
            '''we found the cutting point in lead: right between lead_r
            and lead_f. Now we find how long is the segment in 'other'
            that will be inserted into lead.'''
            
            '''if lead_f is None, then lead_r is the last element of 
            lead, therefore, we just attach everything from other at the
            end of lead; and we are done.'''
            if lead_f == None:    
                lead_r.next = other_r
                return result_head
                
            '''try to expand the segment in other by moving other_f
            forward for as long as other_f.val could be before
            lead_f.val. Var other_m (middle) keeps track of the node
            before other_f'''
            other_m = other_r
            while other_f != None and other_f.val <= lead_f.val:
                other_m = other_f
                other_f = other_f.next

            '''other_m is now the last element in the segment of other
            that goes between lead_r and lead_f. Now we patch the
            pointers.
            lead : 1   2\            / 6   8   9
            other:       \ 3   4   5/  7
            '''
            lead_r.next = other_r
            other_m.next = lead_f
            
            ''' if other_f is null, then there is nothing else in other,
            then, we are done.'''
            if other_f == None:
                break

            '''If lead_f is null AND other_f is still something (we did
            not brake above), we attach the remainder of other to the
            end last element of lead (other_m) before exiting.'''
            if lead_f == None:
                other_m.next = other_f
                break

            '''If none of them is null, then there is more work to do.'''
            lead_r,other_r = lead_f,other_f
            lead_f,other_f = lead_f.next,other_f.next
        return result_head
