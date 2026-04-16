n= int(input())

# Please write your code here.
def is_range(row,col):
    return (0<=row<n)&(0<=col<n)

def change_dir(d_idx, row, col):
    for i in range(4):
        if i != (d_idx+2)%4:
            nx, ny = dir[i]
            X = row+nx
            Y = col+ny
            if is_range(X,Y) and grid[Y][X] != -1:
                return d_idx
    d_idx = (d_idx+1)%4
    return d_idx


grid = [[-1 for _ in range(n)] for _ in range(n)]
dir = [(1,0), (0,-1), (-1,0), (0,1)]
cnt,row,col = 1, (n-1)//2, (n-1)//2
dir_idx = 3
grid[col][row] = cnt

while cnt < n**2:
    cnt += 1
    dir_idx = change_dir(dir_idx, row, col)

    nx, ny = dir[dir_idx]
    row += nx
    col += ny
    grid[col][row] = cnt
    

for row in grid:
    print(*row)
    


    