from array import array
from random import random

floats = array('d', (random() for _ in range(10 ** 7)))
print(floats[-1])


# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
#
# fp = open('floats.bin', 'rb')
# floats2 = array('d')
# floats2.fromfile(fp, 10**7)
# fp.close()
# print(len(floats2))
# print(floats2[-1])