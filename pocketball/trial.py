import math
# w1, w2, t1, t2, h1, h2의 각 x,y 좌표
r = 2.865   # 공의 반지름
w1, w2 = list(int(input().split()))
t1, t2 = list(int(input().split()))
h1, h2 = list(int(input().split()))


def find_seta(w1, w2, t1, t2, h1, h2):
    # 일직선에 있으면...? 
    if (w2-t2)/(w1-t1) == (t2-h2)/(t1-h1):
        seta = 0 #????????????????????????
    else:
        x = h1 - w1
        y = h2 - w2
        seta1 = math.atan(x/y)

        a = math.sqrt(x**2 + y**2)
        b = math.sqrt((h1 - t1)**2 + (h2-t2)**2)
        c = math.sqrt((t1-w1)**2 + (t2-w2)**2)

        seta3 = math.acos((a**2 + b**2 - c**2) / 2*a*b)

        d = math.sqrt(a**2 + (b+2*r)**2 - 2*a*(b+2*r)*math.cos(seta3))

        seta2 = math.acos(((a**2)+(b+2*r)**2 - d**2) / 2*a*(b+2*r))

        seta = seta1 + seta2
    return seta


seta_input = find_seta(w1, w2, t1, t2, h1, h2)




