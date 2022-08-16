def bin_search(arr, l, r, value):
	
	if r >= 1:
		mid = l + (r - l) // 2
		if value == arr[mid]:
			return value	
		return bin_search(arr, 1, mid-1, value) if value < arr[mid] else bin_search(arr, mid+1, r, value)
	else:
		return -1

def ternary_search(arr, l, r, value):
	if r >=1:
		mid1 = l + (r-l)//3
		mid2 = r - (r-l)//3

		if value == arr[mid1]:
			return value
		elif value = arr[mid2]:
			return value
		else:
			if value < arr[mid1]:
				return ternary_search(arr, 1, mid1=1, value)
			elif value > arr[mid2]:
				return ternary_search(arr, mid2+1, r, value)
			else:
				return ternary_search(arr, mid1+1, mid2-1, value)


#k = math.sqrt(len(arr))
def jump_search(arr, l, k, value):
	if value == arr[l]:
		return value
	elif value < arr[l+k]:
		return linear_search(arr[l, l+k], value)
	else:
		return jump_search(arr, l+k, k, value)


def interpolation_search():
	"""
	m = arr[hi] - arr[low]/ (hi-low)
	y = mx + c --(i)
	arr[hi] = m*hi + c --(2)
	arr[lo] = m*lo + c ---(3)
	y - arr[lo] = m(x - lo)
    y = 

	"""

def exponential_search(arr, i, n, value):
	if arr[0] == value:
		return value

	while i < n and arr[i] < value:
		i *= 2
	else:
		return -1

	return linear_search(arr, i//2, min(i, n-1), value)

def min_2_item(arr):
	min1 = min2 = 10000000000000
	for i in arr:
		if i < min1:
			min2 = min1
			min1 = i
		elif min1 < i and i < min2:
			min2 = i
	return min1, min2


def findMax(arr):
	max = -1
	i = 0
	while i < len(arr) and arr[i] < 


if __name__ == '__main__':
	arr = range(11)
	print(bin_search(arr, 19))