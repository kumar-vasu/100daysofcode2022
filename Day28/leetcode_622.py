class MyCircularQueue:

    def __init__(self, k: int):
        self.c_queue = [0]*k
        self.front = -1
        self.rear = -1
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = 0
            self.rear = (self.rear+1) % self.length
            self.c_queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front+1) % self.length
            return True

    def Front(self) -> int:
        if self.front >= 0:
            return self.c_queue[self.front]
        else:
            return self.front

    def Rear(self) -> int:
        if self.rear >= 0:
            return self.c_queue[self.rear]
        else:
            return self.rear

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.front == 0 and self.rear == self.length-1) or(self.front - self.rear == 1):
            return True
        return False
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()