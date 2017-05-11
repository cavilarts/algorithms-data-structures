# Uses python 3

# Alignment Game
# Input: Two strigns
# Output: A longest common subsequence of these strings

def alignment_game(A, B):
	A = list(A)
	B = list(B)

	D = [[0 for x in range(len(B))] for y in range(len(A))]

	for k in range(len(D[0])):
		D[0][k] = k

	for l in range(len(D)):
		D[l][0] = l

	for j in range(len(D[0])):
		for i in range(len(D)):
			insertion = D[i][j - 1] + 1
			deletion = D[i - 1][j] + 1
			match = D[i - 1][j - 1]
			mismatch = D[i - 1][j - 1] + 1

			if(A[i] == B[j]):
				D[i][j] = min(insertion, deletion, match)
			else:
				D[i][j] = min(insertion, deletion, mismatch)

	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in D]))

print(alignment_game("EDITING", "DISTANCE"))

