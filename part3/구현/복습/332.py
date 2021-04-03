from itertools import combinations

n, m = map(int, input().split())
h_positions = []
ck_positions = []

result = 1e9
arr = []


# c : 치킨집 좌표 ((0, 1), (1,2)) ((0, 1), (1,2))
def get_ck_distance(c):
    distance = 0

    for home in h_positions:
        min_value = 1e9
        for ck in c:
            dist = abs(ck[0] - home[0]) + abs(ck[1] - home[1])
            min_value = min(min_value, dist)
        distance += min_value
        if distance > result:
            return 1e9
    return distance


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            h_positions.append((i, j))
        elif row[j] == 2:
            ck_positions.append((i, j))

    arr.append(row)

for i in range(m, 0, -1):
    coms = list(combinations(ck_positions, m))

    for c in coms:
        sum_distance = get_ck_distance(c)
        result = min(result, sum_distance)
print(result)
