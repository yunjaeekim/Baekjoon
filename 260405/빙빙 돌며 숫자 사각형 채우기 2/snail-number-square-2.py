n, m = map(int, input().split())

# Please write your code here.

def is_range(r,c):
    return (0<=r<m)&(0<=c<n)

def is_keep(r,c):
    if is_range(r,c):
        if grid[c][r] == -1:
            return True
    return False
        

def move(dir_idx,r,c):
    nx,ny = dir[start_dir]
    new_r,new_c = r+nx, c+ny
    if is_keep(new_r,new_c):
        return start_dir, new_r,new_c
    else:
        idx = (dir_idx+1)%4
        nx,ny = dir[idx]
        return idx, r+nx, c+ny

dir = [(0,1),(1,0),(0,-1),(-1,0)] #down, right, up, left
start_dir,x,y,cnt = 0,0,0,1
grid = [[-1 for _ in range(m)] for _ in range(n)]
ans = ''

while cnt <= m*n:
    grid[y][x] = cnt
    start_dir,x,y = move(start_dir,x,y)
    cnt += 1

for row in grid:
    print(*row)


    
