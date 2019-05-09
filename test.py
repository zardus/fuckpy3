import fuckpy3

def test():
	import os
	for _ in range(10000):
		s = os.urandom(8)
		assert s.str().bytes() == s
		assert s.hex().unhex() == s
		assert s.str().hex().unhex() == s

if __name__ == '__main__':
	test()
