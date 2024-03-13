lst = [0, 1, 1]
number = int(input())
n = 3

while True:
    if number in (1,2,3):
        print(lst[number-1])
        break
    elif n == number:
        print(lst[n-1])
        break
    else:
        lst.append(0)
        lst[n] = lst[n-1] +1
        if (n+1) % 6 == 0:
            lst[n] = min(lst[(n+1)//2 -1]+1,lst[(n+1)//3 -1]+1, lst[n])
        elif (n+1) % 2 == 0:
            lst[n] = min(lst[(n+1)//2 -1]+1, lst[n])
        elif (n+1) % 3 == 0: 
            lst[n] = min(lst[(n+1)//3 -1]+1, lst[n])
        n += 1