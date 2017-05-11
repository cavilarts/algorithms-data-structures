def knapsack_iterator(W, V, m):
	value = [0] * (m + 1)

	for w in range(m + 1):
		for i in range(len(W)):
			if(W[i] <= w):
				val = value[w - W[i]] + V[i]
				if(val > value[w]):
					value[w] = val

	return value


print(knapsack_iterator([6, 3, 4, 2], [30, 14, 16, 9], 10))

