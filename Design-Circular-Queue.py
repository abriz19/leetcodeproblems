class MyCircularQueue:

    def __init__(self, k: int):
        # Initialize queue with fixed size k
        self.queue = [0] * k
        self.k = k
        self.front = 0  # Points to the front element
        self.rear = -1  # Points to the last element
        self.count = 0  # Number of elements in the queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move rear pointer circularly
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Move front pointer circularly
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
