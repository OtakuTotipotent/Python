def evenGenerator(limit):
    for l in range(2, limit + 1, 2):
        yield(l)

for n in evenGenerator(20):
    print(n)