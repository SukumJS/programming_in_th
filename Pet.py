score = [0]
for i in range(5):
    score.append(sum([int(x) for x in input().split()]))
maximum = score.index(max(score))
print(maximum, max(score))
