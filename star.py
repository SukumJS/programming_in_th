import math
flag = 0
N = int(input())
row = math.ceil(N/2)
temp = 1

for i in range(1, row+1):
    if i == 1:
        print("-" * (row - i) + "*" + "-" * (row - i))
    else:
        print("-" * (row - i) + "*" + "-" * temp + '*' + "-" * (row - i))
        temp += 2
temp -= 2
for i in range(row, 0, -1):
    if i == row and flag == 0 and N % 2 != 0:
        flag = 1
        temp -= 2
        continue
    elif i == 1:
        print("-" * (row - i) + "*" + "-" * (row - i))
    else:
        print("-" * (row - i) + "*" + "-" * temp + '*' + "-" * (row - i))
        temp -= 2
print("")
