K = int(input())
lst = []
minus_1 = 0
minus_2 = 0
for _ in range(6):
    dir, dist = map(int, input().split())
    lst.append((dir, dist))
garo = sero = 0
for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > garo:
            garo = lst[i][1]
    if lst[i][0] == 3 or lst[i][0] == 4:
        if lst[i][1] > sero:
            sero = lst[i][1]

for i in range(6):
    if lst[i%6][0] == 1 and lst[(i+1)%6][0] != 4:
        minus_1, minus_2 = lst[i%6][1], lst[(i+1)%6][1]
    if lst[i%6][0] == 2 and lst[(i+1)%6][0] != 3:
        minus_1, minus_2 = lst[i%6][1], lst[(i+1)%6][1]
    if lst[i%6][0] == 3 and lst[(i+1)%6][0] != 1:
        minus_1, minus_2 = lst[i%6][1], lst[(i+1)%6][1]
    if lst[i%6][0] == 4 and lst[(i+1)%6][0] != 2:
        minus_1, minus_2 = lst[i%6][1], lst[(i+1)%6][1]
print((garo*sero-minus_1*minus_2)*K)