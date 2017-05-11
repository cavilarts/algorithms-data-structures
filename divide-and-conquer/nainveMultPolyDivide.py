def mult_poly(A, B):
	n = len(A)
	pol = [0] * (n - 1)

	if(n == 1):
		pol[0] = A[a] * B[b]
		return pol
	else:
		print("TODO implement normal")

	return pol

def karatsuba(A, B, n):
	k = []
	if(n < 1):
		k.append(A[0] * B[0])
	else:
		m = n//2
		print(m)
		a = karatsuba(A[:m], B[:m], m)
		b = karatsuba(B[m:], B[m:], m)
		c = karatsuba(a, b, m)

			
	return k
print(karatsuba([5, 6, 7, 8], [1, 2, 3 ,4], 4))
#print(mult_poly([4, 3, 2, 1], [1, 2, 3, 4]))
