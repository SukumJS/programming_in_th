ball = 1
swap = input()
for i in swap:
    if i == 'A' and ball != 2 and ball != 3:
        ball = 2
        continue
    if i == 'A' and ball != 1 and ball != 3:
        ball = 1
        continue
    if i == 'B' and ball != 3 and ball != 1:
        ball = 3
        continue
    if i == 'B' and ball != 2 and ball != 1:
        ball = 2
        continue
    if i == 'C' and ball != 3 and ball != 2:
        ball = 3
        continue
    if i == 'C' and ball != 1 and ball != 2:
        ball = 1
        continue
print(ball)
