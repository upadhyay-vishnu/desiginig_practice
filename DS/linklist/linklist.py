from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

def getLL(ll):
    while ll:
        print(ll.data)
        ll = ll.next

def insert_node_at_end(node, ll):
    while ll.next:
        ll = ll.next
    ll.next = node

def insert_node_at_first(node, ll):
    temp = ll.head
    ll.head = node
    node.next = temp

def insert_node_after_a_node(node, ll, value):
    while ll.next:
        if ll.data == value:
            break
        ll = ll.next
    if not ll.next and ll.data != value:
        return
    temp = ll.next
    ll.next = node
    node.next = temp
    return True


def length_of_ll(ll):
    #check of empty ll
    if not ll.next:
        return 0

    count = 1
    while ll.next:
        count += 1
        ll = ll.next
    return count

def length_of_ll_recusively(ll, count=0):
    if not ll:
        return count
    else:
        count += 1
        return length_of_ll_recusively(ll.next, count)

def loop_in_ll(ll):
    slow = ll
    fast = ll
    # check of empty ll
    if not ll.next:
        return 0
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def length_of_loop(ll):
    pass

def create_loop(ll, value):
    loop_node = None
    count = 1
    my_list = ll
    while ll.next:
        if ll.data == value:
            loop_node = ll
        ll = ll.next
        count += 1
    ll.next = loop_node
    for _ in range(count):
        print(my_list.data)
        my_list = my_list.next
    print(my_list.data)

def intersection_of_sorted_ll(ll, ll):
    new_list = LinkedList()
    min_1, min_2 = -1, -1
    min_1_node, min_2_node = None, None
    while ll.next:
        if min_1 > ll.data:
            min_node = ll
            min_1 = ll.data
        ll = ll.next
    while ll.next:
        if min_1 > ll.data:
            min_node = ll
            min_1 = ll.data
        ll = ll.next

    while ll == min_1_node:
        ll = ll.next
    while ll == min_2_node:
        ll = ll.next

    new_list.head(ll)
    while ll.next or ll.next:
        if ll.data < ll.data:
            pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    ll.head.next = second
    second.next = third
    fourth = Node(4)
    insert_node_at_end(fourth, ll.head)
    fifth = Node(5)
    insert_node_at_first(fifth, ll)
    sixth = Node(6)
    insert_node_after_a_node(sixth, ll.head, 5)
    insert_node_after_a_node(Node(7), ll.head, 4)
    # getLL(ll.head)
    print(length_of_ll(ll.head))
    print(length_of_ll_recusively(ll.head))
    create_loop(ll.head, 2)
