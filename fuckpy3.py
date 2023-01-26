import platform
import logging
import codecs

_str_encode = str.encode
_bytes_decode = bytes.decode

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

def _b_encode(x, e, *_, **__):
	if e == 'hex':
		return x.hex()
	raise AttributeError("encode")
def _s_encode(x, e, *args, **kwargs):
	if e == 'hex':
		return x.hex()
	return _str_encode(x, e, *args, **kwargs)
def _b_decode(x, e, *args, **kwargs):
	if e == 'hex':
		return x.unhex()
	return _bytes_decode(x, e, *args, **kwargs)
def _s_decode(x, e, *_, **__):
	if e == 'hex':
		return x.unhex()
	raise AttributeError("decode")

if platform.python_implementation() == "CPython":
	import forbiddenfruit

	forbiddenfruit.curse(bytes, "str", _str)
	forbiddenfruit.curse(str, "bytes", _bytes)
	forbiddenfruit.curse(str, "str", _nop)
	forbiddenfruit.curse(bytes, "bytes", _nop)

	forbiddenfruit.curse(bytes, "unhex", _unhex)
	forbiddenfruit.curse(str, "unhex", _unhex)
	forbiddenfruit.curse(str, "hex", _hex)

	forbiddenfruit.curse(str, "encode", _s_encode)
	forbiddenfruit.curse(bytes, "encode", _b_encode)
	forbiddenfruit.curse(str, "decode", _s_decode)
	forbiddenfruit.curse(bytes, "decode", _b_decode)
else:
	logging.error("Unsupported python variant.")
