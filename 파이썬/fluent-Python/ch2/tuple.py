# Tuple 은 "필드 명이 없는 레코드" 로 간주하고 사용할 수도 있다!

lax_coordinates = (33.94, -118.3242)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567")]
for passport in sorted(traveler_ids):
    print("{}/{}".format(*passport))

for country, _ in traveler_ids:
    print(country)

import os

print(
    os.path.split(
        "/home/hby/cloud-computing-intel-it-architecting-software-as-a-service-paper.pdf"
    )
)

_, filename = os.path.split(
    "/home/hby/cloud-computing-intel-it-architecting-software-as-a-service-paper.pdf"
)
print(filename)

a, b, *rest = range(5)  # 0, 1, [2, 3, 4
a, b, *rest = range(3)  # 0, 1, [2]
a, b, *rest = range(2)  # 0, 1, []
a, *rest, b, c = range(6)  # 0, [1, 2, 3], 4, 5
a, *rest, b = range(2)  # 0, [], 1


# 내포된 튜플 언패킹

metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.689722, 77.691667)),
]

print("{:15} | {:^9} | {:^9}".format("", "lat", "long"))
fmt = "{:15} | {:^9} | {:^9}"

for name, cc, pop, (lat, long) in metro_areas:
    print(fmt.format(name, lat, long))


from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.132314, 139.1312314))
print(tokyo)
print(tokyo[0], tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi_NCR', 'IN', 21.935, LatLong(28.61231, 77.243242))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())

print(set(list.__dict__) - set(tuple.__dict__))