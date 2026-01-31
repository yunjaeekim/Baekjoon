n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
ans = ['']*2*n*max(x)
crr = n*max(x)
w_cnt, b_cnt, g_cnt = 0,0,0
for dst, drt in zip(x, dir):
    if drt == 'L':
        ans[crr-dst+1:crr+1] = [i+'L' for i in ans[crr-dst+1:crr+1]]
        crr -= dst-1
    else:
        ans[crr:crr+dst] = [i+'R' for i in ans[crr:crr+dst]]
        crr += dst-1

for word in ans:
    if word == '':
        continue
    R_cnt = 0
    L_cnt = 0
    for sp in word:
        if sp == 'L':
            L_cnt += 1
        else:
            R_cnt += 1
    if (R_cnt >= 2) & (L_cnt >= 2):
        g_cnt += 1
    else:
        if word[-1] == 'R':
            b_cnt += 1
        else:
            w_cnt += 1

print(w_cnt, b_cnt, g_cnt)
    

        