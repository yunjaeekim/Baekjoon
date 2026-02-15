N, M = map(int, input().split())

a_arr, b_arr = [], []

# Please write your code here.
def move(arr, N):
    pos = 0
    for _ in range(N):
        v, t = map(int, input().split())
        while t>0:
            pos += v
            arr.append(pos)
            t -= 1

move(a_arr, N)
move(b_arr, M)

time, max_time = 0, len(a_arr)
winner, ans = "", 0

while time < max_time:
    if a_arr[time] > b_arr[time]:
        if winner != "A":
            ans += 1
        winner = "A"
    
    elif a_arr[time] < b_arr[time]:
        if winner != "B":
            ans += 1
        winner = "B"

    else:
        if winner != "AB":
            ans += 1
        winner = "AB"
    time += 1

print(ans)
