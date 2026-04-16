n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def cnt_pos(lst,upper_lst):
    if len(lst) == 0:
        return 0

    flag = len(upper_lst) == 0

    if len(lst) == 1:
        if flag:
            return 1

        pos = lst[0]
        for upp in upper_lst:
            if abs(pos-upp) >2:
                return 1
        return 0
    
    past = lst.pop()
    for pos in lst:
        if pos-past >2:
            for upp in upper_lst:
                if abs(pos-upp) >2:
                    return 2
            past = pos
        past = pos
    return 1


ans = {0:0, 1:0, 2:0, 3:0}
for row in range(n):
    lst_1, lst_2, lst_3 = [], [], []
    for col in range(n-2):
        val = arr[row][col] + arr[row][col+1] + arr[row][col+2]
        if val == 3:
            lst_3.append(col+1)
        elif val == 2:
            lst_2.append(col+1)
        elif val == 1:
            lst_1.append(col+1)
    
    ans[3] += cnt_pos(lst_3,[])

    if ans[2] < 2:
        ans[2] += cnt_pos(lst_2,lst_3)
    if ans[1] < 2:
        ans[1] += cnt_pos(lst_1, lst_2+lst_3)

    if ans[3] >= 2:
        print(6)
        break

def cal_score(score, num):
    if num == 0:
        return score

    if score >= (num+1)*2:
        return score
    
    if score > 0:
        if ans[num] >= 1:
            return score + num
        return cal_score(score,num-1)
    
    if ans[num] >= 2:
        return num*2
    
    elif ans[num] == 1:
        return cal_score(num, num-1)
    
    else:
        return cal_score(score,num-1)

print(cal_score(0,3))


