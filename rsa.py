def generate_keys(p, q):
	if not isCorrect(p, q):
		return (None, None)

	n = p * q
	fi = euler_func(p, q)

	from random import choice
	try:
		e = choice(get_e(fi))
		d = choice(get_d(fi, e))
	except:
		return None, None

	public_key = (e, n)
	private_key = (d, n)

	return public_key, private_key

def get_d(fi, e, max_k = 10000):
	ds = []
	for k in range(1, max_k):
		d_up = (fi*k + 1) 
		if d_up % e == 0:
			d = d_up // e
			ds.append(d)
	return ds

def get_e(fi):
	es = []
	for i in range(1, fi+1):
		if gcd(i, fi) == 1 and isPrime(i):
			es.append(i)
	return es

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def euler_func(p, q):

	return (p - 1) * (q - 1)

def isCorrect(p, q):

	return isPrime(p) and isPrime(q)

def isPrime(num):
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

def encrypt(msg, public_key):
	e, n = public_key

	msg = list(map(ord,msg))

	new_msg = []
	for num in msg:
		new_msg.append(pow(num, e, n))

	new_msg = list(map(str, new_msg))
	return " ".join(new_msg)

def decrypt(msg, private_key):
	d, n = private_key

	msg = list(map(int, msg.split()))

	new_msg = []
	for num in msg:
		new_msg.append(pow(num, d, n))

	new_msg = list(map(chr, new_msg))
	return "".join(new_msg)

