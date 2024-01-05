num_list = [int(x) for x in input().split()]
num_list = sorted(num_list)
sort = input()
for i in sort:
    match i:
        case 'A':
            print(num_list[0], end=" ")
        case 'B':
            print(num_list[1], end=" ")
        case 'C':
            print(num_list[2], end=" ")
