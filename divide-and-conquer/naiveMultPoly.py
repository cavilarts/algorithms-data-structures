def mult_poly(A, B, n):
	product = [0] * (2 * n - 1)
	
	for i in range(0, n):
		for j in range(0, n):
			product[i + j] = (A[i] * B[j]) + product[i + j]

	return product

print(mult_poly([4, 3, 2, 1], [1, 2, 3, 4], 4))
