import math
N = int(input())
intt = math.floor(math.log(N,2))
if math.log(N,2) == intt:
    print(N)
else:
    print(2*(N-2**(intt)))