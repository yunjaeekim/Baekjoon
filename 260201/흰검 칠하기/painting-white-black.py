n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
ans = [0]*2*n*max(x)
crr = n*max(x)
w_cnt, b_cnt, g_cnt = 0,0,0
for dst, drt in zip(x, dir):
    if drt == 'L':
        ans[crr-dst+1:crr+1] = [i+1 for i in ans[crr-dst+1:crr+1]]
        crr -= dst-1
    else:
        ans[crr:crr+dst] = [i+10000 for i in ans[crr:crr+dst]]
        crr += dst-1

for idx, val in enumerate(ans):
    black = val // 10000
    white = val % 10000
    if val == 0:
        continue
    elif (black >= 2) & (white >= 2):
        g_cnt += 1
    elif idx >= crr:
        if black > white:
            b_cnt += 1
        else:
            w_cnt += 1
    else:
        if white > black:
            w_cnt += 1
        else:
            b_cnt += 1

print(w_cnt, b_cnt, g_cnt)
    

        