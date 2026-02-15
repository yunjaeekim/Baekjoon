n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
def make_arr(dir_arr, dis_arr):
    arr, pos = [], 0
    while len(dir_arr) > 0:
        dir, dis = dir_arr.pop(0), dis_arr.pop(0)
        if dir == 'R':
            while dis > 0:
                pos += 1
                arr.append(pos)
                dis -= 1
        else:
            while dis > 0:
                pos -= 1
                arr.append(pos)
                dis -= 1
    return arr

A_max, B_max = sum(t), sum(t_b)
flag = A_max > B_max

A_pos, B_pos = 0, 0
A_arr = make_arr(d, t)
B_arr = make_arr(d_b, t_b)

time,ans = 0, 0

if flag:
    while time < A_max:
        A_past, B_past = A_pos, B_pos
        A_pos = A_arr[time]
        if time < B_max:
            B_pos = B_arr[time]

        if A_pos == B_pos:
            if A_past != B_past:
                ans += 1

        time += 1
else:
    while time < B_max:
        A_past, B_past = A_pos, B_pos
        B_pos = B_arr[time]
        if time < A_max:
            A_pos = A_arr[time]
        
        if A_pos == B_pos:
            if A_past != B_past:
                ans += 1

        time += 1

print(ans)




