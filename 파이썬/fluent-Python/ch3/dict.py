import collections

my_dict = {}


print(isinstance(my_dict, collections.abc.Mapping))
print(list(zip([1, 2, 3], [4, 5, 6])))


a = {}
print(a.setdefault('a', []))
print(a.setdefault('a', []).append(1))
print(a)

from collections import defaultdict