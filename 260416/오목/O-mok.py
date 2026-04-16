import sys
board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def is_range(x,y):
    return (0<=x<19)&(0<=y<19)

def is_five(dir,x,y):
    start = board[x][y]
    dx,dy = dir
    for _ in range(4):
        x += dx
        y += dy
        if not is_range(x,y):
            return False, 0
        if board[x][y] != start:
            return False, 0
    return True, start

dir = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
flag = False

for row in range(19):
    for col in range(19):
        start = board[row][col]
        if start == 0:
            continue
        else:
            for d in dir:
                flag, color = is_five(d,row,col)
                if flag:
                    print(color)
                    print(row+d[0]*2+1,col+d[1]*2+1)
                    sys.exit()
print(0)
