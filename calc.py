from collections import OrderedDict


class Calculator(object):
	def __init__(self):
		self.operators = "*/+-"

	@staticmethod
	def eval_operator(token_list, operator):
		try:
			ope_index = token_list.index(operator)
		except ValueError:
			return False

		if operator == "+":
			token_list[ope_index - 1] = token_list[ope_index - 1] + token_list[ope_index + 1]
		elif operator == "-":
			token_list[ope_index - 1] = token_list[ope_index - 1] - token_list[ope_index + 1]
		elif operator == "*":
			token_list[ope_index - 1] = token_list[ope_index - 1] * token_list[ope_index + 1]
		elif operator == "/":
			token_list[ope_index - 1] = token_list[ope_index - 1] / token_list[ope_index + 1]
		else:
			raise NotImplementedError("{} is not a know operator".format(operator))
		del token_list[ope_index]
		del token_list[ope_index]
		return True

	def calc(self, input_str):
		tokens = [i.strip() for i in input_str.split()]
		for i, token in enumerate(tokens):
			try:
				tokens[i] = float(token)
			except ValueError:
				pass
		return self.calc_string(tokens)

	def calc_string(self, tokens):
		while "(" in tokens:
			start = tokens.index("(")
			end = tokens.index(")")
			tokens[start] = self.calc_string(tokens[start + 1:end])
			for i in range(end - start):
				del tokens[start + 1]
		while len(tokens) > 1:
			for i in self.operators:
				if self.eval_operator(tokens, i):
					continue
		return tokens[0]

	def calc_with_vars(self, input_list):
		vars = OrderedDict()
		for item in input_list:
			if "=" in item:
				tokens = [i.strip() for i in item.split("=")[1].strip().split()]
				for index, token in enumerate(tokens):
					try:
						tokens[index] = float(token)
					except ValueError:
						pass
				vars[item.split()[0].strip("=")] = tokens
		for var in vars:
			for index, i in enumerate(vars[var]):
				if type(i) is not float:
					if i not in self.operators:
						vars[var][index] = vars[i]
			vars[var] = self.calc_string(vars[var])
		return [vars[i] for i in vars]

if __name__ == '__main__':
	calc = Calculator()
	print calc.calc("3 + 4 * 5 / 7")
	print calc.calc("3 + 4 * 5")
	print calc.calc("( 3 + 4 ) * 5 / 7")
	print calc.calc_with_vars(
		["pi = 3",
		"pizza = 9 * 9 * pi",
		"a = pizza * 2"])