# fuckpy3

In the vein of [fuckpep8](https://github.com/zardus/fuckpep8), a misguided attempt to make the world conform to my view of how things should work, rather than the actual reality.

Makes this possible (thanks to [forbiddenfruit](https://github.com/clarete/forbiddenfruit)):

```
>>> import fuckpy3
>>> 'asdf'.bytes()
b'asdf'
>>> b'asdf'.str()
'asdf'
>>> 'asdf'.str() # for convenience, so you don't have to think about what data type something _was_
'asdf'
>>> b'asdf'.bytes() # for convenience, so you don't have to think about what data type something _was_
b'asdf'
>>> 'asdf'.hex()
b'61736466'
>>> b'asdf'.hex() # python built-in
'61736466'
>>> b'asdf'.hex().unhex()
b'asdf'
>>> 'asdf'.hex().unhex()
b'asdf'
>>> 'asdf'.hex().unhex().str()
'asdf'
```

# FAQ

## Why?

Because it's the right thing to do.

## pypy?

This is all based on the amazing forbiddenfruit, so pypy support will magically happen if forbiddenfruit gets pypy support.

## thanks i hate it
