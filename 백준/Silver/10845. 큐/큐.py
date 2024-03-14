def push(number):
    global lst
    list = [0.1]
    list[:-1] = lst
    list[-1] = number
    lst = list

def pop():
    global lst
    if len(lst) == 0:
        print(-1)
    else:
        num = lst[0]
        lst = lst[1:]
        print(num)

def size():
    global lst
    print(len(lst))

def empty():
    global lst
    if len(lst) == 0:
        print(1)
    else:
        print(0)

def front():
    global lst
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[0])

def back():
    global lst
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])

import sys
input = sys.stdin.readline
number = int(input())
list = [input().split() for i in range(number)]
lst = []
for i in list:
    if i[0] == 'push':
        push(i[1])
    elif i[0] == 'front':
        front()
    elif i[0] == 'pop':
        pop()
    elif i[0] == 'size':
        size()
    elif i[0] == 'empty':
        empty()
    else:
        back()