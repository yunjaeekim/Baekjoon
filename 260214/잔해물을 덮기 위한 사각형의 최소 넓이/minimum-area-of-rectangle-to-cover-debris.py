x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
min_x, max_x, min_y, max_y = min(x1), max(x2), min(y1), max(y2)
mat = []
def possible(max, min, low_corr, high_corr):
    if (min < low_corr[0]) & (max > high_corr[0]):
        return False, 0
    else:
        cur_corr = min
        while True:
            if (cur_corr >= low_corr[0]):
                if (cur_corr <= low_corr[1]) | (cur_corr >= high_corr[1]):
                    break
            cur_corr += 1
        start_x = cur_corr

        while True:
            if (cur_corr >= high_corr[0]):
                if (cur_corr <= low_corr[1]) | (cur_corr >= high_corr[1]):
                    break
            cur_corr += 1
        if cur_corr == high_corr[1]:
            cur_corr = low_corr[1]
        end_x = cur_corr
        return True, end_x - start_x

x, y = [], []
for curr_y in range(y1[0], y2[0]+1):
    if (y1[1] <= curr_y <= y2[1]):
        flag, value = possible(max_x, min_x, x1, x2)
        if flag:
            x.append(value)
    else:
        x.append(x2[0]-x1[0])
        break

for curr_x in range(x1[0], x2[0]+1):
    if (x1[1] <= curr_x <= x2[1]):
        flag, value = possible(max_y, min_y, y1, y2)
        if flag:
            y.append(value)
    else:
        y.append(y2[0]-y1[0])
        break

print(max(y)*max(x))
