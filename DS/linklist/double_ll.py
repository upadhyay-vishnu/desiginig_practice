class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None


    def insert_at_first(self, node):
        if not self.head:
            self.head = node

    def insert_at_head(self, node):
        if not self.head:
            self.insert_at_first(node)
        node.next = self.head
        self.head.pre = node.next
        self.head = node

    def this_is_new_f(self):
        pass

    def insert_at_end(self, node):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        node.prev = ptr
        ptr.next = node
        ptr = node

    def insert_after_node(self, node, value):
        ptr = self.head
        while ptr.next and ptr.data != value:
            ptr = ptr.next

        if(ptr.data==value):
            node.next = ptr.next
            ptr.next = node
            ptr = node

    def insert_before_node(self, node, value):
        ptr = self.head
        prev = None

        while ptr.next and ptr.data != value:
            prev = ptr
            ptr = ptr.next

        # print(prev.data, ptr.data)
        if(ptr.data == value):
            if prev:
                print("here1")
                prev.next = node
                node.next = ptr
                prev = node
            else:
                print("here2")
                node.next = ptr
                prev = node
                ptr.prev = node
                

    def traverse(self): 
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def delete_front_node(self, value):
        ptr = self.head
        if ptr:
            while ptr.next and ptr.data != value:
                ptr = ptr.next

            if ptr.data == value:
                if not ptr.prev:
                    ptr = ptr.next
                    ptr.prev = None
                    self.head = ptr

                else:
                    if not ptr.next:
                        temp = ptr
                        ptr = ptr.prev
                        ptr.next = None
                    else:
                        temp = ptr
                        ptr.prev.next = temp.next
                        temp.next.prev = ptr.prev.next
                        self.head = ptr.next

    def reverse_ll(self):
        if not self.head:
            return
        ptr = None
        while self.head.next:
            ptr = self.head
            self.head = self.head.next

                        
dll = DLL()
dll.insert_at_first(Node(1))
# dll.insert_at_head(Node(2))
# dll.insert_at_head(Node(3))
dll.insert_after_node(Node(2), 1)
dll.insert_after_node(Node(3), 2)
dll.insert_at_end(Node(4))
# dll.insert_after_node(Node(5), 3)
# dll.insert_before_node(Node(6), 1)
# dll.insert_before_node(Node(8), 3)
# dll.delete_front_node(3)
# dll.delete_front_node(4)
# dll.delete_front_node(6)
dll.traverse()
