import sys
input = sys.stdin.readline
count = int(input())
lst = [int(input()) for i in range(count)]
stack, num, Flag, answer = [], 0, True, ""

for i in range(count):
    number = lst[i]

    if number > num:
        answer += "+\n" * (number-num)
        answer += "-\n"
        for i in range(number-num):
            num += 1
            stack.append(num)
        stack.pop()
    else:
        if number == stack[-1]:
            answer += "-\n"
            stack.pop()
        else:
            Flag = False
            break
if Flag:
    print(answer)
else:
    print("NO")    