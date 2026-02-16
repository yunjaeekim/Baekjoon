n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
nx, ny = [-1,0,0,1], [0,-1,1,0]

def in_range(n,r,c):
    return (1<=r<=n) & (1<=c<=n)

def print_state(r,c):
    return (arr[r-1][c-1] == 1)

for _ in range(m):
    r,c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1
    state = 0
    for i in range(4):
        x = c+nx[i]
        y = r+ny[i]
        if in_range(n,y,x):
            state += print_state(y,x)
    if state == 3:
        print(1)
    else:
        print(0)    