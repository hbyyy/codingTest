from collections.abc import Sequence, Container, Iterable, Sized


symbols = "#$%^&*)"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 40]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 40, map(ord, symbols)))
print(beyond_ascii)