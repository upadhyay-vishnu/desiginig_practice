class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def build_tree(root, left, right):
	root.left = left
	root.right = right

def traverse_seq(inorder, preorder):
	pass


def is_sibling(root, a, b):
	if root is None:
		return 0
	return (root.left==a and root.right==b) or 
			(root.left==b and root.right==a) or
            (is_sibling(root.left, a, b)) or 
             (is_sibling(root.right, a, b))

    #def this_is_new(self):
    #    d = 'anbc'
    #    return d
def level(root, node, lev=1):
	if root is None:
		return 0
	if root == node:
		return lev

	l = level(root.left, node, lev+1)
	if l != 0:
		return l
	return level(root.right, node, lev+1)


