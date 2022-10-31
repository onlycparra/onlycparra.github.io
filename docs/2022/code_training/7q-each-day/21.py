# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode], \
                      list2: Optional[ListNode]) \
                      -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        # let list1 be the one with the smallest (or equal) starting
        # value out of the two lists.
        list_runner,list_insert = (list1,list2) \
            if list1.val < list2.val \
               else (list2,list1)
        ans = list_runner

        # breaks when there is nothing else to insert in list_runner.
        while list_insert != None:
            # list_runner points to its furthest element smaller or equal
            # than value at list_insert. After this while loop, list_runner
            # is at the end of its contiguous segment. Between
            # list_runner and list_runner.next, a portion of list_insert
            # will be inserted.
            while list_runner.next != None and \
                  list_runner.next.val <= list_insert.val:
                list_runner = list_runner.next

            # means that we reached the end of list_runner and still the
            # last element was smaller or equal than the current in
            # list_insert. Therefore, we just append the whole list_insert
            # at the end of list_runner.
            if list_runner.next == None:
                list_runner.next = list_insert
                break

            # ――――――――lr――lrac―――――
            # li―――――――
            list_runner_after_cut = list_runner.next
            
            # ――――――――lr┐ lrac―――――
            #           └―li―――――――
            list_runner.next = list_insert

            # ――――――――――┐ li―――――――
            #           └―lr―――――――
            list_runner,list_insert = list_insert,list_runner_after_cut

        return ans
