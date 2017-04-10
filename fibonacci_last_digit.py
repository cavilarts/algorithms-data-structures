# Uses python3

def calc_fib(num):
	a,b = 0, 1 

	if (num > 100):
		num = num % 60

	for n in range(num):
		a, b = b, a + b
	
	return a % 10

n = int(input())
print(calc_fib(n))
