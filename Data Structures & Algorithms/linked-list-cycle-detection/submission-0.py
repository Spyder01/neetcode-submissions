# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        rabbit, turtle = head, head 

        while turtle is not None and rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            turtle = turtle.next

            if rabbit == turtle:
                return True

        return False