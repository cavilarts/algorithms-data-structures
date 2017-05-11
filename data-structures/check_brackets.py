# python3

import sys

class Bracket:
	def __init__(self, bracket_type, position):
		self.bracket_type = bracket_type
		self.position = position

	def Match(self, c):
		if self.bracket_type == '[' and c == ']':
			return True
		if self.bracket_type == '{' and c == '}':
			return True
		if self.bracket_type == '(' and c == ')':
			return True
		return False

if __name__ == "__main__":
	text = sys.stdin.read()

	opening_brackets_stack = []
	for i, next in enumerate(text):
		if next == '(' or next == '[' or next == '{':
			opening_brackets_stack.append(next)
		if next == ')' or next == ']' or next == '}':
			a = Bracket(next, i)
			if (len(opening_brackets_stack) > 0):
				top = opening_brackets_stack.pop()
				a.Match(top)
	if('a' in locals()):
		if(len(opening_brackets_stack)):
			print(a.position)
		else:
			print(i)
	else:
		print("Success")
