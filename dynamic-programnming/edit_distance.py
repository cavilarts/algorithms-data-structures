# Uses python3
def edit_distance_c(s, t):
	A = list(s)
	B = list(t)
	D = [[0 for x in range(len(B) + 1)] for y in range(len(A) + 1)]
	
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
			
			if(A[i - 1] == B[j - 1]):
				D[i][j] = min(insertion, deletion, match)
			else:
				D[i][j] = min(insertion, deletion, mismatch)
	print(levenshteinDistance(s, t))
	print(D)
	return D[i][j]

def edit_distance(s1, s2):
	if len(s1) > len(s2):
		s1, s2 = s2, s1

	distances = range(len(s1) + 1)
	for i2, c2 in enumerate(s2):
		distances_ = [i2+1]
		for i1, c1 in enumerate(s1):
			if c1 == c2:
				distances_.append(distances[i1])
			else:
				distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))

		distances = distances_

	return distances[-1]

if __name__ == "__main__":
	 print(edit_distance(input(), input()))
