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
