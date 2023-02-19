def check(num):
    check_num = list(str(num))
    length = len(check_num)
    for i in range(length-1):
        if check_num[i] > check_num[i+1]:
            return -2
    return num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mx = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = lst[i]*lst[j]
            if check(num) > mx:
                mx = check(num)
    print(f'#{tc} {mx}')
