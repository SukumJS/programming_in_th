import math
stride, distance = [int(x) for x in input().split()]
n = distance//stride
if distance < stride:
    print(2)
else:
    print(n + math.ceil((distance-n*stride) / stride))
