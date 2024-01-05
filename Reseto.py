n, k = map(int, input().split())
temp = 0
num_list = []
dashed = [0, 1]
for i in range(2, n+1):
    num_list.append(i)
while len(dashed) != n+1:
    p = num_list[temp]
    for i in range(len(num_list)):
        if num_list[i] % p == 0 and num_list[i] not in dashed:
            dashed.append(num_list[i])
    temp += 1
print(dashed[k+1])
