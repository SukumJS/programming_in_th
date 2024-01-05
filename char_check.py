words = input()
flag = 0

for i in words:
    if i > 'A' and i < 'Z':
        if flag == 2:
            flag = 0
            break
        flag = 1
    if i > 'a' and i < 'z':
        if flag == 1:
            flag = 0
            break
        flag = 2

match flag:
    case 1:
        print("All Capital Letter")
    case 2:
        print("All Small Letter")
    case 0:
        print("Mix")
