def inorder(root):
    while not root:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def insert(root, value):
    q = []
    if not root.left and not root.right:
        root.data = Tree(value)
    else:
        q.append(root)
        while q:
            temp = q[0]
            q.pop()
            if temp.left:
                q.append(temp.left)
            else:
                temp.left = Tree(value)
                break
            
            if temp.right:
                q.append(temp.right)
            else:
                temp.right = Tree(value)
                break

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1

def height_balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh) <=1 and height_balanced(root.left) and height_balanced(root.right):
        return True
    return False

s = []
def create_stack(root):
    while root:
        s.append(root)
        print(root.data, end=' ')
        root = root.left

def inorder_on_stack(root):
    create_stack(root)
    current = None
    if current is None and s:
        current = s.pop()
        print('--', current.data)
        current = current.right
    else:
        create_stack(current)

def diagonal_tree_traversal(root):
    q = []
    left_q =[]
    while root:
        root = root.right
        q.append(root)
        left_q.append(root.left)

    while q:
        root = q.pop(0)
        print(root.data)
        q.append(root.left)
    

def level(root, node, lev=1):
    if root is None:
        return 0
    if root.data == node:
        return lev

    l = level(root.left, node, lev+1)
    if l != 0:
        return l
    return level(root.right, node, lev+1)


def is_sibling(root, a, b):
    if root is None:
        return 0
    return (root.left==a and root.right==b) or (
            root.left==b and root.right==a) or (
             is_sibling(root.left, a, b)) or (
              is_sibling(root.right, a, b))


def is_cousin(root, node1, node2):
    node1_level = level(root, node1)
    node2_level = level(root, node2)

    return (node1_level == node2_level) and not (is_sibling(root, node1, node2))


def get_all_leaves(root):
    pass


def sum_tree(root):
    if root is None:
        return root.data
    sum_tree(root.left) == sum_tree(root.right)

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if __name__ == '__main__':
    # root = Tree(10)
    # root.left = Tree(11)
    # root.left.left = Tree(7)
    # root.right = Tree(9)    
    # root.right.left = Tree(15)
    # root.right.right = Tree(8)
    root = Tree(8)
    root.left = Tree(3)
    root.right = Tree(10)
    root.left.left = Tree(1)
    root.left.right = Tree(6)
    root.right.right = Tree(14)
    root.right.right.left = Tree(13)
    root.left.right.left = Tree(4)
    root.left.right.right = Tree(7)

    # print(level(root, 3))
    print(is_cousin(root, 3, 13))
    print(get_all_leaves(root))

    # inorder(root)
    # # insert(root, 12)
    # print('\n')
    # inorder(root)
    # print('\n')
    # print("height is: ", height(root))

    # inorder_on_stack(root)
                    


