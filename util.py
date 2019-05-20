from parser import show, parse

def repl():
	while True:
		s = input('>>> ').strip()
		if s == ':q':
			break
		try:
			o = parse(s)
			print(show(o))
		except Exception as e:
			print('Parsing error:' + str(e))


if __name__ == "__main__":
	repl()