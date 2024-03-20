#filter는 찾아야되는 수들의 모든 index를 알려줌! find와는 나오는 값의 첫번째 값!
#string에서 replace를 쓰면 시간 복잡도가 심하다!
#while 문은 log, for 문은 n 이다.
import sys
input = sys.stdin.readline
count = int(input())
lst = [list(input()) for i in range(count)]
answer = 0
    
for i in range(count):
    lst_Y = list(filter(lambda x: lst[i][x] == "Y", range(count)))
    total = lst_Y.copy()
    
    for j in lst_Y:
        new_lst = list(filter(lambda x: lst[j][x] == "Y", range(count)))   
        
        total += new_lst 
    if len(set(total))-1 > answer:
        answer = len(set(total))-1
    else:
        pass

print(answer)