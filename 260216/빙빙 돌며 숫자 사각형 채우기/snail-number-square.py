n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
def keep_move(arr,m,n,r,c):
    if (1<=r<=n) & (1<=c<=m):
        if arr[r-1][c-1] == 0:
            return True
    return False

def turn(arr,r,c):
    return (arr[r][c] != 0)

step = {
    0:(0,1),
    1:(1,0),
    2:(0,-1),
    3:(-1,0)
}
r,c,dir = 1,1,0
arr[0][0] = "1"

for i in range(2,n*m+1):
    nr,nc = step[dir]
    if keep_move(arr,m,n,r+nr,c+nc):
        r += nr
        c += nc
        arr[r-1][c-1] = str(i)
    else:
        dir = (dir+1) % 4
        nr,nc = step[dir]
        r += nr
        c += nc
        arr[r-1][c-1] = str(i)

for i in range(n):
    print(*arr[i])
