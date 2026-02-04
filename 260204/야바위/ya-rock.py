n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
stone = {}
cup = {1:'one', 2:'two', 3:'three'}
for (a,b,c) in moves:
    cup_a, cup_b = cup[b], cup[a]
    cup[a] = cup_a
    cup[b] = cup_b
    stone[cup[c]] = stone.get(cup[c], 0) + 1

ans_stone = max(stone, key=stone.get)

if ans_stone == 'one':
    print(1)
elif ans_stone == 'two':
    print(2)
else:
    print(3)
