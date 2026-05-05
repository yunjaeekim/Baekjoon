N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def is_range(x,y):
    return (0<=x<N)&(0<=y<N)

def move(cur_dir, x, y, alp):
    if alp == 'F':
        dx, dy = dir[cur_dir]
        if is_range(x+dx, y+dy):
            return cur_dir, (x+dx, y+dy), True
        else:
            return cur_dir, (x, y), False

    else:
        if alp == 'L':
            cur_dir = (cur_dir+3)%4
        else:
            cur_dir = (cur_dir+1)%4
        return cur_dir, (x,y), False


x, y, cur_dir = N//2, N//2, 0
dir = [(-1,0), (0,1), (1,0), (0,-1)]
ans = board[x][y]

for alp in str:
    cur_dir, (x, y), flag = move(cur_dir, x, y, alp)
    if flag:
        ans += board[x][y]

print(ans)