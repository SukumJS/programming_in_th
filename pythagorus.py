import math
a, b = input().split()
a, b = float(a), float(b)
c = math.sqrt(pow(a, 2) + pow(b, 2))
print("{:.6f}".format(c))
