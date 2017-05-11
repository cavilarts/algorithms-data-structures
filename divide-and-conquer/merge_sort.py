import math

def merge_sort(array):
	n = len(array)

	if(n == 1):
		return array
	
	if(n > 1):
		m = int(n/2)
		B = merge_sort(array[:m])
		C = merge_sort(array[m:])
		A = merge_array(B, C)
		return A

def merge_array(A, B):
	d = []
	print(A, B, "<< Yolo")
	while(True):
		if(len(A) == 0 and len(B) == 0):
			break

		if(b <= c):
			d.append(b)
			d.append(c)
		else:
			d.append(c)
			d.append(b)

		A.pop(0)
		B.pop(0)

	return d

print(merge_sort([7, 2, 5, 3, 13, 1, 6]))
