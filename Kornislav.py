n = area = 0
trace = [int(x) for x in input().split()]
trace = sorted(trace, reverse=True)
edge = [0, 0, 0, 0]

for i in range(0, 5, 3):
    if trace[i] == 2:
        edge[n] += 2

    else:
        edge[n] += trace[i]
        n += 1
for i in range(1, 3):
    if trace[i] == 2:
        edge[n] += 2

    else:
        edge[n] += trace[i]
        n += 1
x = min(edge[1], edge[3])
y = min(edge[0], edge[2])
area = x * y
print(area)
