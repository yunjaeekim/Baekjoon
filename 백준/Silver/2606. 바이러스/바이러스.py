import sys
input = sys.stdin.readline
number = int(input())
count = int(input())
connect = [sorted(list(map(int,input().split()))) for _ in range(count)]
n,lst,answer,ans = count,[],[0]*number,0
answer[0] = 1
while n > 0:
    if connect[n-1][0] == 1:
        lst.append(connect[n-1][1])
        answer[connect[n-1][1]-1] = 1
        ans += 1
    n -= 1

while True:
    if len(lst) == 0:
        break
    else:
        num = lst.pop()
        n = count
        while n > 0 :
            num_1 = connect[n-1][0]
            num_2 = connect[n-1][1] 
            if num_1 == num:
                if answer[num_2-1] == 0:
                    lst.append(num_2)                    
                    answer[num_2-1] = 1
                    ans += 1
            if num_2 == num:
                if answer[num_1-1] == 0:
                    lst.append(num_1)
                    answer[num_1-1] = 1
                    ans += 1

            n -= 1

print(ans)