distinct_modlist = []
for i in range(10):
    num = int(input())
    if num % 42 not in distinct_modlist:
        distinct_modlist.append(num % 42)
print(len(distinct_modlist))
