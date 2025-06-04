# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        while cur:
            if cur.val < x:
                ltail.next = cur
                ltail = ltail.next
            else:
                rtail.next = cur
                rtail = rtail.next
            cur = cur.next
        ltail.next = right.next
        rtail.next = None
        return left.next
      
        