# Uses python3
import sys
import random

def get_optimal_value(capacity, weights, values):
	density = compute_density(values, weights)
	indexes = density_index(density)
	value = 0.
	capacity_max = capacity

	print(weights, "<< weights")
	print(values, "<<values")
	print(density, "<< density")
	print(indexes, "<< indexes")
	
	for i in range(len(density)):
		if(capacity_max <= 0):
			break

		if(weights[indexes[i]] > capacity_max):
			weight =  (capacity_max - capacity) + capacity
			value = value + ((values[indexes[i]] / weights[indexes[i]]) * capacity)
		else:
			weight = weights[indexes[i]]
			value = value + values[indexes[i]]

		capacity_max = capacity_max - weight

	return value

def density_index(density):
	a = []
	indexes = []

	for i in range(len(density)):
		a.append(i)

	indexes = [x for (y,x) in sorted(zip(density, a), reverse=True)]

	return indexes

def compute_density(values, weights):
	density = []

	for i in range(len(values)):
		density.append(values[i] / weights[i])

	return density

def test_cases():
	while True:
		length = random.randint(1, 1000)
		capacity = random.randint(1, 2000000)
		values = []
		weights = []

		for i in range(length):
			values.append(random.randint(1, 2000000))
			weights.append(random.randint(1, 2000000))
		
		print(get_optimal_value(capacity, weights, values), "<<<<< mine output")	

#test_cases()

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
