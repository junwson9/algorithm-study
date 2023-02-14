import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
arr.sort(key = lambda x:(x[1], x[0]))
cnt = 1
fin = arr[0][1]
for i in range(1,N):
    if fin <= arr[i][0]:
        cnt += 1
        fin = arr[i][1]
print(cnt)
