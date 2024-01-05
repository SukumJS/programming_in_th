in_num = int(input())
my_dict = {}
nums = input().split()

for i in nums:
    num = int(i)
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

max_frequency = max(my_dict.values())
mode = [key for key, value in my_dict.items() if value == max_frequency]
sorted_mode = sorted(mode)

for i in sorted_mode:
    print(i, end=" ")
