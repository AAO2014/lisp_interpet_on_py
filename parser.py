import re
from ptypes import keywords_vk, Symbol, nil, car, cdr, cons, ConsListClass, isnull


def prsval(s):
	if s == 'true':
		return True
	elif s == 'false':
		return False
	elif s in keywords_vk:
		return keywords_vk[s]
	else:
		try:
			return int(s)
		except Exception:
			try:
				return float(s)
			except Exception:
				return Symbol(s)


def prslist(s):
	s = s.lstrip()
	if not s:
		raise ValueError('closed \')\' is absent')
	elif s[0] == ')':
		return nil, s[1:]
	else:
		x, ss = prs(s)
		t, zz = prslist(ss)
		return cons(x, t), zz


def subs(s): 
	return s if len(s) < 20 else s[0:20] + '...'


def prs(s):
	s = s.lstrip()
	if not s:
		return nil, ''

	c, z = s[0], s[1:]
	if c == '(':
		return prslist(z)
	elif c == ')':
		raise ValueError('extra closed \')\': ' + subs(s))
	elif c == '\"':
		try:
			a, b = re.search('\"', z).span()
			return z[0:a], z[b:]
		except Exception:
			raise ValueError('closed \'\"\' is absent: ' + subs(s))
	elif c == ';':
		try:
			a, b = re.search(';', z).span()
			return prs(z[b:])
		except Exception:
			raise ValueError('closed \';\' is absent: ' + subs(s))
	elif c == '\'':
		x, ss = prs(z)
		return cons(SF.QUOTE, cons(x, nil)), ss
	else:
		a, b = re.search('\s|\(|\)|\"|;|$', s).span()
		return prsval(s[0:a]), s[a:]


def parse(s):
	x, ss = prs(s)
	if not ss.strip():
		return x
	y, zz = prs('(' + ss + ')')
	if not zz.strip():
		return cons(x, y)
	else:
		raise ValueError('extra symbols: ' + subs(zz))


def show(o):
	if isinstance(o, ConsListClass):
		r = ''
		while not isnull(o):
			r, o = r + ' ' + show(car(o)), cdr(o)
		return '(' + r.lstrip() + ')'
	elif o in keywords_vk:
		return keywords_vk[o]
	elif isinstance(o, Symbol):
		return o.value
	elif isinstance(o, bool):
		return'true' if o else 'false'
	elif isinstance(o, str):
		return '"' + o + '"'
	else:
		return str(o)
