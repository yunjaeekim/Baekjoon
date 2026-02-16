n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def possible(n,r,c):
    return r-1>=0,c-1>=0,r+1<n,c+1<n

def check(arr, n, r, c):
    cnt = 0
    L,D,R,U = possible(n, r, c)
    if L:
        cnt += (arr[c][r-1]==1)
    if D:
        cnt += (arr[c-1][r]==1)
    if R:
        cnt += (arr[c][r+1]==1)
    if U:
        cnt += (arr[c+1][r]==1)
    return cnt>=3

ans = 0
for c in range(n):
    for r in range(n):
        ans += check(grid, n, r, c)
print(ans)