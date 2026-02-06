x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
M_x1, M_x2 = min(x1), max(x2)
M_y1, M_y2 = min(y1), max(y2)

mat = [[0]*(M_x2-M_x1)]*(M_y2-M_y1)

x1 = [i-M_x1 for i in x1]
x2 = [i-M_x1-1 for i in x2]
y1 = [i-M_y1 for i in y1]
y2 = [i-M_y1-1 for i in y2]

for i in range(len(x1)):
    if i == len(x1)-1:
        mat = [
            [
                0 if (x1[i] <= col <= x2[i]) & (y1[i] <= row <= y2[i]) else mat[row][col]
                for col in range(len(mat[0]))
            ]
        for row in range(len(mat))
        ]
    
    else:
        mat = [
            [
                1 if (x1[i] <= col <= x2[i]) & (y1[i] <= row <= y2[i]) else mat[row][col]
                for col in range(len(mat[0]))
            ]
        for row in range(len(mat))
        ]

print(sum([sum(row) for row in mat]))