length = 0
number = int(input())
VPS = [list(map(str,input())) for i in range(number)]
vps = []
for i in range(number):
    vps = [1 if x == '(' else -1 for x in VPS[i]]
    if len(vps) % 2 != 0:
        print("NO")
    elif vps[0] == -1 or vps[-1] == 1:
        print("NO")
    else:
        while True:
            if len(vps) == 0:
                print("YES")
                length = 0
                break
            elif length == len(vps):
                print("NO")
                length = 0
                break
            else:
                vps_1 = vps.copy()
                vps_1.pop(0)
                vps_1.append(0)
                index = []
                length = len(vps)
                for idx,val in enumerate(zip(vps,vps_1)):
                    if val[0]>0 and val[0]*val[1] == -1:
                        index.append(idx)
                        index.append(idx+1)
                for i,j in enumerate(index):
                    del vps[j-i]