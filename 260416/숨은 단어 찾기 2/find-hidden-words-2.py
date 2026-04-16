N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
def is_range(x,y):
    return (0<=x<N)&(0<=y<M)

mv = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
ans = 0

for row in range(N):
    for col in range(M):
        for dx,dy in mv:
            X,Y = row+dx*2,col+dy*2
            if is_range(X,Y):
                if arr[row][col]+arr[row+dx][col+dy]+arr[X][Y] == 'LEE':
                    ans += 1

print(ans)