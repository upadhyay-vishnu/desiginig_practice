class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    # Inorder
    def traverse(self, root):
        if (not root):
            return
        self.traverse(root.left)
        print(root.data)
        self.traverse(root.right)

    def queue_insert(self, root, node):
        if not root:
            root = node
            return

        q = []
        q.append(root)
        while q:
            temp = q[0]
            q.pop(0)
            if temp.left:
                q.append(temp.left)
            else:
                temp.left = node
                break

            if temp.right:
                q.append(temp.right)
            else:
                temp.right = node
                break

    def delete_node(self, root, node):
        # search deleted node
        if root.data == node:
            dltd_node = root
            return dltd_node
        else:
            delete_node(root.left)
            delete_node(root.right)

    def right_deepest_node(self, root):
        while root.right:
            root = root.right
        else:
            if root.left:
                right_deepest_node(root.left)

        temp = root
        temp = delete_node()
        del root



if __name__ == '__main__':
    t = Tree(Node(23))
    t.queue_insert(t.root, Node(24))
    t.queue_insert(t.root, Node(25))
    t.queue_insert(t.root, Node(26))
    t.traverse(t.root)
    # t.insert(t, Tree(25))
