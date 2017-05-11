def knapsack_wo_rep(W, V, m):
	values = [[0 for x in range(m + 1)] for y in range(len(W))]
	
	for i in range(len(W)):
		for w in range(m + 1):
			values[i][w] = values[i - 1][w]
			if(W[i] <= w):
				val = values[i - 1][w - W[i]] + V[i]
				if(values[i][w] < val):
					values[i][w] = val

	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
	 	for row in values]))

	
	return ""

print(knapsack_wo_rep([6, 3, 4, 2], [30, 14, 16, 9], 10))
