def fractional_knapsack(capacity, cargo):
    pack = []
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    total = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total += p[1]
        else:
            total += p[0] * capacity
            break
    return total

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
    ]

r = fractional_knapsack(15, cargo)
print(r)
