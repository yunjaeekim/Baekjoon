n, m = map(int, input().split())

# Please write your code here.
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
            'R','S','T','U','V','X','Y','Z']
grid = [[-1 for _ in range(m)] for _ in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
cur_dir, x, y, cnt = 0,0,0,0

def is_keep(cur_dir,x,y):
    nx,ny = dir[cur_dir]
    new_x, new_y = x+nx, y+ny
    if (0<=new_x<m)&(0<=new_y<n):
        if grid[new_y][new_x] == -1:
            return cur_dir, new_x,new_y
    
    new_dir = (cur_dir+1)%4
    nx,ny = dir[new_dir]
    return (cur_dir+1)%4, x+nx, y+ny


while cnt < n*m:
    grid[y][x] = alphabet[cnt%25]
    cur_dir,x,y = is_keep(cur_dir,x,y)
    cnt += 1

for row in grid:
    print(*row)
    


