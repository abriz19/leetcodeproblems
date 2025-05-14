class ListNode:
    def __init__(self, val, ):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.leftNode = ListNode(0)
        self.rightNode = ListNode(0)
        self.leftNode.next = self.rightNode
        self.rightNode.prev = self.leftNode

    def get(self, index: int) -> int:
        cur = self.leftNode.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.rightNode and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.leftNode.next, self.leftNode
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.rightNode, self.rightNode.prev
        next.prev = node    
        prev.next = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.leftNode.next 
        while cur and index > 0:
            index-=1
            cur = cur.next
        if index == 0 and cur:
            node, next, prev = ListNode(val), cur, cur.prev
            next.prev = node    
            prev.next = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.leftNode.next 
        while cur and index > 0:
            index-=1
            cur = cur.next
        if index == 0 and cur and cur != self.rightNode:
            next, prev =  cur.next, cur.prev
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(1)
# print(param_1)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
