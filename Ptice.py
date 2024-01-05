score_list = [["Adrian", 0], ["Bruno", 0], ["Goran", 0]]

score = int(input())
ans = input()

Adrian = "ABC" * 40
Bruno = "BABC" * 40
Goran = "CCAABBCC" * 40

for i in range(len(ans)):
    if Adrian[i] == ans[i]:
        score_list[0][1] += 1
    if Bruno[i] == ans[i]:
        score_list[1][1] += 1
    if Goran[i] == ans[i]:
        score_list[2][1] += 1

score_max = [score_list[0][1], score_list[1][1], score_list[2][1]]
score_max.sort()
print(max(score_max))
for i in range(3):
    if score_list[i][1] == max(score_max):
        print(score_list[i][0])
