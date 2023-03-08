N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
ans = 0
first = [0, 1, 2]*(N//3)    #맨처음 상태 카드 만들기 012 012 012 이순서로 뿌린다
suffle = [0]*len(first)

i = 0
while True:
    if first == P:      #지민이가 원하는데로 보내면 끝
        break
    suffle[i] = first[S[i]] #셔플에다가 S에 적힌 순서대로 first에서 가져와 넣을거임
    i += 1
    if i == len(suffle):    #한번 다 섞으면 ans에 1추가
        ans += 1
        if ans == 1:
            check = suffle  #1번 섞었을 때 카드상태를 check라는데다가 저장(계속 섞어도
                            # 답안나올때 쓸거임)
        first = suffle
        suffle = [0]*len(first)# 섞인상태에서 다시 S에 적힌순서로 돌려야 하기때문에 섞인 suffle을 first로, suffle 다시 초기화
        i = 0
        if ans != 1 and first == check: # 섞인suffle이 들어온 first 즉, 1번 이상 섞어봤는데 이값이 check랑 같다? 이건 카드를 처음섞은 상태로 돌아왔다는 거니까 답이 P가 될수가 없음
            ans = -1
            break
print(ans)