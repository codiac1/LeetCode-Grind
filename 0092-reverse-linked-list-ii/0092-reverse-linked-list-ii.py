# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        if left == right :
            return head 

        dummy = ListNode(-1 , head)
        leftPrev = dummy
        curr = head

        for i in range(left -1 ):
            leftPrev = leftPrev.next
            curr = curr.next

        sublistHead = curr
        prev = None

        for i in range(right - left + 1):
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd

        leftPrev.next = prev
        sublistHead.next = curr

        

        return dummy.next


        
