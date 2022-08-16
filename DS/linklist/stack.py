from sys import maxsize


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = []
        self.middle = None

    def is_empty(self):
        if self.array:
            return False

    def is_full(self):
        if len(self.array) == self.max_size:
            return True

    def push(self, value):
        if self.is_full():
            return
        self.array.append(value)

    def pop(self):
        if not self.is_empty():
            return self.array.pop()
        return - (self.max_size + 1)

    @property
    def top(self):
        if self.array:
            return len(self.array)
        return - (self.max_size + 1)

    @property
    def get_middle(self):
        if not self.is_empty():
            return int(0 + (self.top - 0) / 2), self.array[int(0 + (self.top - 0) / 2)]
        return

    def pop_middle(self):
        middle = self.get_middle
        self.array.pop(middle)


class MinStack(Stack):
    def push(self, value):
        if not self.array:
            self.array.append(value)
        else:
            top = self.top
            if value <= top:
                self.array.append(value)

    def pop(self, value):
        while True:
            if self.top > value:
                self.pop()
            break

    def get_min(self):
        return self.top


if __name__ == '__main__':
    l = Stack(5)
    s = MinStack(5)
    l.push(4)
    # s.push(4)
    l.push(2)
    # s.push(2)
    l.push(3)
    # s.push(3)
    l.push(2)
    l.push(3)
    l.push(2)
    l.push(3)
    # s.pop(l.pop())
    # s.pop(l.pop())
    l.push(10)
    # print(l.array)
    # print(s.array)
    print(l.is_empty())
    print(l.array, l.top)
    print(l.get_middle)
    print(s.get_min())
