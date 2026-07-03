# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        count = 0

        curr = head

        while curr is not None:
            count += 1
            curr = curr.next

        curr = head

        target = count - n + 1
        prev = None
        while curr is not None:
            target -= 1
            
            if target == 0:
                if prev is None:
                    head = head.next
                else:                
                    prev.next = curr.next

                break
                

            prev = curr
            curr = curr.next
        
        return head
        