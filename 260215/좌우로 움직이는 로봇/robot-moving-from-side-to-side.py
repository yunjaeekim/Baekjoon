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
def check(past, A_pos, B_pos, ans):
    if A_pos == B_pos:
        if past:
            return True, ans
        else:
            return True, ans + 1
    else:
        return False, ans

def walk(position, direction, distance):
    if distance == 0:
        return position, distance
    if direction == 'R':
        return position+1, distance-1
    else:
        return position-1, distance-1

past, ans = True, 0

A_pos, B_pos = 500000, 500000
A_dir, A_dis = d.pop(0), t.pop(0)
B_dir, B_dis = d_b.pop(0), t_b.pop(0)

while True:
    if A_dis == 0:
        if len(d) > 0:
            A_dir, A_dis = d.pop(0), t.pop(0)
    if B_dis == 0:
        if len(d_b) > 0:
            B_dir, B_dis = d_b.pop(0), t_b.pop(0)
    
    A_pos, A_dis = walk(A_pos, A_dir, A_dis)
    B_pos, B_dis = walk(B_pos, B_dir, B_dis)

    if (A_dis == 0) & (B_dis == 0) & (max(len(d), len(d_b)) == 0):
        break

    past, ans = check(past, A_pos, B_pos, ans)

print(ans)




