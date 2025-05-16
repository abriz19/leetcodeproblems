# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            size1 = size2 = 0
            cur1, cur2 = l1, l2
            while cur1 or cur2:
                if cur1:
                    cur1 = cur1.next
                    size1+=1
                if cur2:
                    cur2 = cur2.next
                    size2+=1
            diff = abs(size1-size2)
            small = l1 if size2>size1 else l2
            large = l2 if size2>size1 else l1
            while diff != 0:
                small = ListNode(val = 0, next = small)
                diff-=1
            small, large = self.reverseList(small), self.reverseList(large)
            two_sum = self.twoSum(small, large)
            return self.reverseList(two_sum)
    def reverseList(self, l: ListNode) -> ListNode:
        cur, prev = l, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def twoSum(self, l1: ListNode, l2: ListNode) -> ListNode:
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



            



        