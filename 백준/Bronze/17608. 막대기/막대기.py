import sys
input = sys.stdin.readline
number = int(input())
lst = [int(input()) for i in range(number)]
max_lst = lst[-1]
max_number = max(lst)
n = 1
for i in range(number-2,-1,-1):
    if max_lst == max_number:
        break
    elif lst[i] == max_number:
        n += 1
        break
    elif lst[i] > max_lst:
        n += 1
        max_lst = lst[i]
print(n)