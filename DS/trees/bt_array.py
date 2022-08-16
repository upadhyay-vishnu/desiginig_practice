tree = [None] * 10

def set_root(key):
	if not tree[0]:
		tree[0] = key

def set_left(key, parent):
	if tree[parent]:
		key_in = 2*(parent) + 1
		tree[key_in] = key
	else:
		print("can't set left")

def set_right(key, parent):
	if tree[parent]:
		key_in = 2*(parent) + 2
		tree[key_in] = key
	else:
		print("can't set right")


if __name__ == '__main__':
	set_root('A')
	set_left('B', 0)
	set_right('C', 0)
	set_left('D', 1)
	set_right('E', 1)
	print(tree)