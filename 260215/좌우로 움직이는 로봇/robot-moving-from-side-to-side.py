n, m = map(int, input().split())

a_arr = []
b_arr = []

def move(arr, k):
    state = 0
    arr.append(state)
    for _ in range(k):
        t, d = input().split()
        t = int(t)

        move = 0
        if d == "R":
            move = 1
        else:
            move = -1

        while t > 0:
            state += move
            arr.append(state)

            t -= 1

move(a_arr, n)
move(b_arr, m)

ans, time = 0,0
A_pos, B_pos= 0,0
A_time, B_time = len(a_arr), len(b_arr)
max_time = max(A_time, B_time)

if A_time > B_time:
    while time < max_time:
        A_past, B_past = A_pos, B_pos
        if time < B_time:
            B_pos = b_arr[time]
        A_pos = a_arr[time]

        if (A_pos == B_pos) & (A_past != B_past):
            ans += 1
        
        time += 1
else:
    while time < max_time:
        A_past, B_past = A_pos, B_pos
        if time < A_time:
            A_pos = a_arr[time]
        B_pos = b_arr[time]

        if (A_pos == B_pos) & (A_past != B_past):
            ans += 1
        
        time += 1

print(ans)

