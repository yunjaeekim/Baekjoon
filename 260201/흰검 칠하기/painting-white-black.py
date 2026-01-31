n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
ans = []
crr, past = 0, 'D'
for dst, drt in zip(x, dir):
    if drt == 'L':
        if drt == past:
            past = 'L'
            for i in range(dst):
                ans.append(crr-i)
            crr -= dst-1
        else:
            past = 'L'
            for i in range(dst):
                ans.append(crr-i)
            crr -= dst-1
    
    else:
        if drt == past:
            past = 'R'
            for i in range(dst):
                ans.append(crr+i)
            crr += dst-1
        else:
            past = 'R'
            for i in range(dst):
                ans.append(crr+i)
            crr += dst-1

cnt = {}
for x in ans:
    cnt[x] = cnt.get(x, 0) + 1

w_cnt, b_cnt, g_cnt = 0, 0, 0

for x, c in cnt.items():
    if c >= 4:
        g_cnt += 1
    
    else:
        if x < 0:
            if c % 2 == 0:
                b_cnt += 1
            else:
                w_cnt += 1
        else:
            if c % 2 == 0:
                w_cnt += 1
            else:
                b_cnt += 1

print(w_cnt,b_cnt,g_cnt)