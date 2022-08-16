class MyQueue:
    def __init__(self, capacity):
        self.rear = self.front = -1
        self.capacity = capacity
        self.occ = -1  # makes life simpler
        self.q = [None] * capacity

    def is_full(self):
        if self.occ == self.capacity - 1:
            print("Queue is full")
            return True

    def is_empty(self):
        if self.occ == -1:
            return True

    def enque(self, value):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.occ += 1

    def deque(self):
        if self.is_empty():
            return
        self.front = (self.front + 1) % self.capacity
        value = self.q[self.front]
        self.q[self.front] = None
        self.occ -= 1
        return value

    def traverse(self):
        print(self.q)

    def on_front(self):
        return self.front

    def on_rear(self):
        return self.rear


if __name__ == '__main__':
    q = MyQueue(5)
    q.enque(1)
    q.enque(2)
    q.enque(1)
    q.enque(2)
    q.enque(2)
    q.enque(2)
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    print(q.on_rear(), q.on_front())
    q.traverse()
