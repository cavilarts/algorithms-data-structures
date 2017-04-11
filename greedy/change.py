# Uses python3
import sys
import random

def get_change(m):
	amount = m
	total_coins = 0
	large, medium, small = 10, 5, 1
	
	for i in range(amount):
		if amount <= 0:
			break
		
		if amount >= large:
			strategy = large

		if amount >= medium and amount < large:
			strategy = medium

		if amount < medium:
			strategy = small
			
		total_coins = total_coins + (amount // strategy)
		amount = amount -  ((amount // strategy) * strategy)			
	
	return total_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

#def main():

#	while True:
#		rand = random.randint(1, 1000)
#		print(rand, "randNum")
#		print(get_change(rand), "<< Output")

#main()
