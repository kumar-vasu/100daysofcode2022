class MyCircularDeque:

    def __init__(self, k: int):
        self.c_queue = [0]*k
        self.front = -1
        self.rear = -1
        self.length = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.rear = 0
                self.front = 0
            else:
                if self.front == 0:
                    self.front = self.length-1
                else:
                    self.front -= 1
            self.c_queue[self.front] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = 0
            self.rear = (self.rear+1) % self.length
            self.c_queue[self.rear] = value
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front+1) % self.length
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                if self.rear == 0:
                    self.rear = self.length-1
                else:
                    self.rear -= 1
            return True

    def getFront(self) -> int:
        if self.front >= 0:
            return self.c_queue[self.front]
        else:
            return self.front

    def getRear(self) -> int:
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


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

        
