x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
min_x, max_x, min_y, max_y = min(x1), max(x2), min(y1), max(y2)
mat = []
for corr_y in range(min_y, max_y+1):
    if (y1[0] <= corr_y < y2[0]):
        if (y1[1] <= corr_y < y2[1]):
            if (min_x < x1[0]) & (max_x > x2[0]):
                pass
            corr_x = min_x
            while True:
                if (corr_x >= x1[0]):
                    if (corr_x <= x1[1]) | (corr_x >= x2[1]):
                        break
                corr_x += 1
            start_x = corr_x
            while True:
                if (corr_x >= x2[0]):
                    if (corr_x <= x1[1]) | (corr_x >= x2[1]):
                        break
                corr_x += 1
            if (corr_x != x2[0]):
                corr_x = min_x
            end_x = corr_x
            mat.append(end_x-start_x)
        else:
            mat.append(x2[0]-x1[0])
print(len(mat)*max(mat))
