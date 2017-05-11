def selection_sort_naive(array):
	for i in range(len(array)):
		min_index = i
		for j in range(i + 1, len(array)):
			if(array[j] < array[min_index]):
				min_index = j

		array[i], array[min_index] = array[min_index], array[i]

	return array

print(selection_sort_naive([5, 9, 6, 15, 2, 14, 4]))
