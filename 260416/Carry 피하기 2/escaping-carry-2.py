n = int(input())
arr = [int(input()) for _ in range(n)]
N = len(str(max(arr)))

# Please write your code here.
def make_lst(num, N):
    lst, K = [], 10**(N-1)
    while K >= 1:
        lst.append(int(num//K))
        num = num % K
        K /= 10
    return lst

def make_num(lst,N):
    idx,num = 1,0
    for val in lst:
        num += val*10**(N-idx)
        idx+=1
    return num

def is_carry(lst):
    for val in lst:
        if val > 9:
            return True
    return False

lst = [make_lst(num,N) for num in arr]
ans = [0,0,0,0]

for i in range(n-2):
    first = lst[i]
    for j in range(i+1,n-1):
        second = lst[j]
        fir_sec = [i+j for i,j in zip(first,second)]
        if not is_carry(fir_sec):
            for k in range(j+1,n):
                third = lst[k]
                cand = [i+j for i,j in zip(fir_sec,third)]
                if not is_carry(cand) and make_num(cand,N)>make_num(ans,N):
                    ans = cand

ans = make_num(ans,N)
if ans == 0:
    print(-1)
else:
    print(ans)
