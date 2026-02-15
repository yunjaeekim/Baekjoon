N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
ans, sh_cnt = [0]*N, {x+1:0 for x in range(N)}
ans[P-1] = 1
handshakes = sorted(handshakes, key=lambda x:x[0])
for (_, a, b) in handshakes:
    if (ans[a-1]==1) & (ans[b-1]==1):
        sh_cnt[a] += 1
        sh_cnt[b] += 1
    
    if (ans[a-1]==1) & (ans[b-1]==0):
        if sh_cnt[a] < K:
            ans[b-1]=1
            sh_cnt[a] += 1
    
    if (ans[b-1]==1) & (ans[a-1]==0):
        if sh_cnt[b] < K:
            ans[a-1]=1
            sh_cnt[b] += 1

print(*ans, sep="") 
