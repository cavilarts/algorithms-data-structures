# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	density = compute_density(values, weights)
	value = 0.
	capacity_max = capacity	
	lol = [weights, values, density]
	print(lol)

	for i in range(capacity):
		if(capacity_max < 1):
			break
		
		#value = value + (a * (values[i] / weights[i]))
		#capacity = capacity_max - value

	return value

def compute_density(values, weights):
	density = []

	for i in range(len(values)):
		density.append(values[i] / weights[i])

	return density

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
