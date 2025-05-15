# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()
        while l1 or l2:
            total = l1.val + l2.val + carry
            val = total % 10
            cur.next = ListNode(val=val)
            cur = cur.next
            carry = total // 10 
            l1 = l1.next
            l2 = l2.next
            if not l1 and l2:
                l1 = ListNode()
            elif not l2 and l1:
                l2 = ListNode()
        if carry != 0:
            cur.next = ListNode(val=carry)

        return dummy.next
        
        