def cons(x, y): return x,y
def car(l): return l[0]
def cdr(l): return l[1]
ConsListClass = tuple

nil = cons(None, None)
def isnull(t): return car(t) is None and cdr(t) is None

class BO(Enum):
	ADD, SUB, MUL, DIV, MOD, SCONCAT = range(6)


class BP(Enum):
	GT, GTE, LT, LTE, EQ, NOEQ = range(6)


class SF(Enum):
	(DEF, SET, GET, QUOTE, TYPEOF, CONS, CAR, CDR, COND, PRINT, READ,
		EVAL, EVALIN, LAMBDA, MACRO, MACROEXPAND) = range(16)

keywords_vk = {
	'+': BO.ADD,
	'-': BO.SUB,
	'*': BO.MUL,
	'/': BO.DIV,
	'mod': BO.MOD,
	'++': BO.SCONCAT,
	'>': BP.GT,
	'>=': BP.GTE,
	'<': BP.LT,
	'<=': BP. LTE,
	'=': BP.EQ,
	'/=': BP.NOEQ,
	'def': BP.DEF,
	'set': BP.SET,
	'get': BP.GET,
	'quote': BP.QUOTE,
	'typeof': SF.TYPEOF,
	'cons': SF.CONS,
	'car': SF.CAR,
	'cdr': SF.CDR,
	'cond': SF.COND,
	'print': SF.PRINT,
	'read': SF.READ,
	'eval': SF.EVAL,
	'eval-in': SF.EVALIN,
	'lambda': SF.LAMBDA,
	'macro': SF.MACRO,
	'macro': SF.MACROEXPAND,	
}

keywords_vk = dict(zip(keywords_vk.values(), keywords_vk.keys()))


class Symbol:
	def __init__(self, s):
		self.value = s
