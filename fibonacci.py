# Uses python3
def calc_fib(num):
	fib_list = []
	
	if (num >= 1):
		for n in range(num):
			if (n <= 1):
				fib_list.append(1)
			else:
				fib_list.append(fib_list[n - 1] + fib_list[n - 2]);
				
		return fib_list[len(fib_list) - 1]
	else:
		return num;

n = int(input())
print(calc_fib(n))
