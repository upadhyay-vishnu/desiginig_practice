class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, node):
        if not self.head:
            self.head = node
            self.head.next = self.head
        else:
            node.next = self.head.next
            self.head.next = node
            self.head = node

    def delete(self, value):
        if not self.head:
            return
        beg = self.head
        ptr = None
        while beg.data != value:
            ptr = beg
            beg = beg.next

        if ptr:
            ptr.next = beg.next
        else:
            while ptr.next != self.head:
                ptr = ptr.next
            self.head = beg.next
        del beg

    def traverse(self):
        beg = self.head
        if self.head:
            while True:
                print(beg.data)
                beg = beg.next
                if beg == self.head:
                    break

    def check_if_SL(self):
        beg = self.head
        while beg.next and beg.next != self.head:
            node = node.next

if __name__ == '__main__':
    ll = CircularLinkedList()
    ll.insertion(Node(1))
    ll.insertion(Node(2))
    ll.insertion(Node(3))
    ll.insertion(Node(4))
    ll.insertion(Node(5))
    ll.delete(5)
    ll.traverse()

