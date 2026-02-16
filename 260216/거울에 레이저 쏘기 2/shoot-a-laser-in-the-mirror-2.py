n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
if 1<=k<=n:
    dir = 1
    r,c = 1,k%n
elif n+1<=k<=2*n:
    dir = 0
    r,c = k%n,n
elif 2*n+1<=k<=3*n:
    dir = 3
    r,c = n, k%n
else:
    dir = 2
    r,c = k%n, 1

dir_to_point = {
    0 : (0,-1),
    1 : (1,0),
    2 : (0,1),
    3 : (-1,0)
}

def change_dir(dir, shape):
    if shape == '/':
        if 0<=dir<=1:
            return 1-dir
        else:
            return 5-dir
    else:
        if (dir==0) & (dir==3):
            return 3-dir
        else:
            return 3-dir

def in_range(n,r,c):
    return (1<=r<=n) & (1<=c<=n)

ans = 0
while (in_range(n,r,c)):
    shape = grid[r-1][c-1]
    dir = change_dir(dir,shape)
    nx,ny = dir_to_point[dir]
    r += nx
    c += ny
    ans += 1
print(ans)


