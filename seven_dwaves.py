in_dwarves = []
sum = 0
for i in range(9):
    num = int(input())
    in_dwarves.append(num)
    sum += num
for i in range(9):
    for j in range(9):
        if sum - 100 == in_dwarves[i] + in_dwarves[j]:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(in_dwarves[k])
