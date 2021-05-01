import platform
import logging

if platform.python_implementation() == "CPython":
        import forbiddenfruit
        import codecs
	import binascii

        def _unhex(x):
                try:
                        return codecs.decode(x, 'hex')
                except binascii.Error:
                        return codecs.decode(x.replace("0x", ""), 'hex')
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
