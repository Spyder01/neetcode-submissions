# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        dummy = ListNode(-1)
        tail = dummy

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
            
            if list1 is None:
                tail.next = list2
                break

            if list2 is None:
                tail.next = list1
                break

        return dummy.next 


        
        