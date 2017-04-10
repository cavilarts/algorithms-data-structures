# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
	if n <= 1:
		return n

	pisano = [0 , 1]
	previous = 0
	current  = 1

	for _ in range(n):
		previous, current = current, previous + current

		if(len(pisano) >= 4 and pisano[len(pisano) - 2] == 0 and pisano[len(pisano) - 1] == 1):
			pisano.pop()
			pisano.pop()
			break
		else:
			pisano.append(current % m)

	return pisano[-1]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
