import math
r = 2.78 # 기억안남..
m = 3   # 마찰계수 임의 지정..
def cal_pocketball(w1, w2, t1, t2, h1, h2):
    # 공이 일직선 상에 있으면 그냥 atan2()써서 angle 반환
    if math.atan2(abs(h1-w1) , abs(h2-w2)) == math.atan2(abs(h1-t1),abs(h2-t2)):
        theta = math.atan2(abs(h1-w1) / abs(h2-w2))
        angle = theta # 각도로 변환....?
         # 홀에 넣으면 초기화될 값이 있을 듯..?
    
    # 타겟공을 쳐서 보내야 되면 acos 사용해야됨
    else:
        theta1 = math.atan2(abs(h1-w1),abs(h2-w2))
        w_h_distance = math.sqrt((h1-t1)**2 + (h2-t2)**2)
        w_t_distance = math.sqrt((t1-w1)**2 + (t2-w2)**2)
        t_h_distance = math.sqrt((h1-t1)**2 + (h2-t2)**2)
        theta3 = math.acos((w_h_distance**2 + t_h_distance**2 - w_t_distance**2) / (2*w_h_distance*t_h_distance) )
        d = math.sqrt(w_h_distance**2 + (t_h_distance+2*r)**2 - math.cos(theta3) * 2*w_h_distance*(t_h_distance+2*r))
        theta2 = math.acos((d**2 + w_h_distance**2 - (t_h_distance+2*r)**2)/(2*d*w_h_distance))
        theta = theta1 + theta2
        angle = theta
        # 얘의 바뀐 좌표는 어케 구하지....?
        # 그냥 한방에 들어갔다고 생각해야 할 듯
    
    power = math.sqrt(t_h_distance *2*m)/math.cos(theta)
    w1, w2 = 0, 0   # 한번에 
    return angle, power, w1, w2