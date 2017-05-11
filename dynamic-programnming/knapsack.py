# Uses python3
import sys

def optimal_weight(W, w):
	values = [[0 for x in range(W + 1)] for y in range(len(w))]

	for i in range(len(w)):
		for j in range(W+ 1):
			values[i][j] = values[i - 1][j]
			if(w[i] <= j):
				val = values[i - 1][j - w[i]] + w[i]
				if(values[i][j] < val):
					values[i][j] = val

	return values[len(w) - 1][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
