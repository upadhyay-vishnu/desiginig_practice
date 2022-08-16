"""
This algo is use to find
Maximum Subarray Sum in an Array
"""
"""
Algo:

ptr->, meh=0, msf=-10000000

Loop through the arr
    -> meh = meh + arr[i]
    -> if meh < a[i]
        -> meh = a[i]
    -> if msf < meh
        msf = meh
"""

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
meh = 0
msf = -10000000
for i in arr:
    meh = meh + i
    if meh < i:
        meh = i
    if meh > msf:
        msf = meh

print(msf)

a = [100, 200, 1, 3, 2, 4]

"""
largest subarray of sum 0
"""

arr = [15, -2, 2, -8, 1, 7, 10, 23]

max_len = -1
_sum = 0
d = {}

for i, v in enumerate(arr):
    _sum = _sum + v
    if _sum in d:
        max_len = i - d[_sum]
    else:
        d[_sum] = i


s = "this is an amazing program"


import string

arr = []
new_s = ''
for i in s.rstrip():
    if i not in string.whitespace:
        new_s += i
    else:
        arr.append(new_s)
        arr.append(i)
        new_s = ''
arr.append(new_s)
i = 0
j = len(arr) - 1
while i <= j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1



from queue import Queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.mag = 0

    def level_order_traversal(self, root):
        q = Queue()
        q.put(root)
        l = []
        while q.queue:
            ptr = q.queue[0]
            l.append(ptr.data if ptr else None)
            q.get()
            if ptr:
                if any([ptr.left, ptr.right]):
                    q.put(ptr.left)
                    q.put(ptr.right)
        return l



def height_of_node(self, node):
    if not node:
        return 0
    return 1+ max(height_of_node(node.left), height_of_node(node.right))


def top_level_view(self, root, hd=0):
    if not root:
        return
    if hd not in self.mp:
        self.mp[hd] = root
    else:
        node = self.mp[hd]
        node_height = self.height_of_node(node)
        root_height = self.height_of_node(root)
        if node_height < root_height:
            self.mp[hd] = node
        else:
            self.mp[hd] = root

    self.top_level_view(root.left, -1-hd)
    self.top_level_view(root.right, 1+hd)


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Linklist:
    def __init__(self):
        self.head = None


def flatten_tree(root, ll):
    if not root:
        return

    if hasattr(ll, 'head'):
        ll.head = root
    else:
        ll.next = root
        ll = ll.next
    flatten_tree(root.left, ll)
    flatten_tree(root.right, ll)


def k_smallest(root, count=0):
    if not root:
        return
    k_smallest(root.left, count+1)
    if count == 3:
        return root
    k_smallest(root.right, count)
