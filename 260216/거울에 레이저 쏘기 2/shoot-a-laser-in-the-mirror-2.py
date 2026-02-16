n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
if 1<=k<=n:         #아래
    r,c = 1,k%n
    nx,ny = 1,0
elif n+1<=k<=2*n:   #왼쪽
    r,c = k%n,n
    nx,ny = 0,-1
elif 2*n+1<=k<=3*n: #위
    r,c = n, 3*n-k+1
    nx,ny = -1,0
else:               #오른쪽
    r,c = 4*n-k+1, 1
    nx,ny = 0,1

def in_range(n,r,c):
    return (1<=r<=n) & (1<=c<=n)

def move(r,c,nx,ny):
    if arr[r-1][c-1] == '/':
        nx,ny = -ny, -nx
    else:
        nx,ny = ny, nx
    return r+nx, c+ny, nx, ny

ans = 0
while in_range(n,r,c):
    r, c, nx, ny = move(r,c,nx,ny)
    ans += 1
print(ans)




