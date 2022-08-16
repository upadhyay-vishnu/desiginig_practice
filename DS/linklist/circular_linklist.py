import time

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class CircularLL:
    def __init__(self):
        self.tail = None

    def add_at_end_cll(self, node):
        """
        End node point to first node, and tail lies on end node
        """
        temp = self.tail
        if not self.tail:
            node.next = node

        else:
            node.next = temp.next
            temp.next = node
        self.tail = node

    def add_at_front_cll(self, node):
        node.next = self.tail.next
        self.tail.next = node

    def delete_node(self, data):

        if not self.tail:
            return
        if self.tail.next == self.tail:
            self.tail = None
            return

        temp = self.tail
        temp = ptr = self.tail
        temp = temp.next
        while temp.data != data:
            ptr = temp
            temp = temp.next
        ptr.next = temp.next

        if temp == self.tail:
            self.tail = ptr
        del temp

    def traverse_cll(self):
        temp = self.tail
        if not self.tail:
            print("CLL is empty")
            return
        temp = temp.next
        count = 1
        print(temp.data)
        while temp != self.tail:
            temp = temp.next
            count += 1
            print(temp.data)

        print("tail is at", self.tail.data)
        print("count is", count)


def check_identical(cll1, cll2):
    h1 = cll1.tail
    h2 = cll2.tail
    count = 0

    h1 = h1.next
    h2 = h2.next
    print(h1.data, h2.data, cll2.tail.data)
    while True:
        time.sleep(2)
        print(h1.data, h2.data, end='->')
        if h1.data == h2.data:
            h1 = h1.next
            count += 1

            if count == 4:
                return True

        else:
            count = 0
            h1 = cll1.tail.next
        if h2 == cll2.tail:
            return False
        h2 = h2.next
        print(h2.data)


if __name__ == '__main__':
    n1 = Node(1)
    cll = CircularLL()
    cll.add_at_end_cll(n1)
    cll.add_at_end_cll(Node(2))
    cll.add_at_front_cll(Node(3))
    cll.add_at_front_cll(Node(4))
    cll.traverse_cll()

    cll.delete_node(4)
    # cll.delete_node(2)
    # cll.delete_node(1)

    cll.traverse_cll()

    cll1 = CircularLL()
    cll1.add_at_end_cll(n1)
    cll1.add_at_end_cll(Node(2))
    cll1.add_at_front_cll(Node(3))
    cll1.add_at_front_cll(Node(4))

    cll2 = CircularLL()
    cll2.add_at_end_cll(Node(1))
    cll2.add_at_end_cll(Node(2))
    cll2.add_at_end_cll(Node(4))
    cll2.add_at_end_cll(Node(3))
    cll2.traverse_cll()

    print(check_identical(cll1, cll2))
