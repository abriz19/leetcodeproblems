# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, l = head, 1
        while curr.next:
            curr = curr.next
            l+=1
        curr = head
        for i in range(l//2):
            curr = curr.next
        return curr

        