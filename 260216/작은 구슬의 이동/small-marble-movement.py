n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
def change_direction(n,r,c):
    return (1<=r<=n) & (1<=r<=n)

nx, ny = [-1,0,0,1], [0,-1,1,0]

if d == 'L':
    idx = 0
elif d == 'R':
    idx = 3
elif d == 'U':
    idx = 2
else:
    idx = 1


for _ in range(t):
    if change_direction(n, c+nx[idx], r+ny[idx]):
        c += nx[idx]
        r += ny[idx]
    else:
        idx = 3 - idx

print(r,c)
