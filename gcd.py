num1, num2 = [int(x) for x in input().split()]
r = max(num1, num2)
while 1:
    if num2 % r == 0 and num1 % r == 0:
        break
    else:
        r -= 1

print(r)
