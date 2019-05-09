import platform
import logging

if platform.python_implementation() == "CPython":
	import forbiddenfruit
	import codecs

	def _unhex(x):
		return codecs.decode(x, 'hex')
	def _bytes(x):
		return codecs.encode(x, 'latin1')
	def _str(x):
		return x.decode('latin1')
	def _hex(x):
		return codecs.encode(x.bytes(), 'hex')
	def _nop(x):
		return x

	forbiddenfruit.curse(bytes, "str", _str)
	forbiddenfruit.curse(str, "bytes", _bytes)
	forbiddenfruit.curse(str, "str", _nop)
	forbiddenfruit.curse(bytes, "bytes", _nop)

	forbiddenfruit.curse(bytes, "unhex", _unhex)
	forbiddenfruit.curse(str, "unhex", _unhex)
	forbiddenfruit.curse(str, "hex", _hex)
else:
	logging.error("Unsupported python variant.")

def test():
	import os
	for _ in range(10000):
		s = os.urandom(8)
		assert s.str().bytes() == s
		assert s.hex().unhex() == s
		assert s.str().hex().unhex() == s
