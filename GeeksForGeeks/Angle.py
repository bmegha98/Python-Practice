'''
Calculate the angle between hour hand and minute hand.
There can be two angles between hands, we need to print minimum of two.
Also, we need to print floor of final result angle. For example, if the final angle is 10.61, we need to print 10.
'''
import math
def Angle(H,M):
    hour=(H*60 +M)*0.5
    minute= M*6
    angle=abs(hour-minute)
    return angle
    
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        HM=list(input().split())
        H,M=eval(HM[0]),eval(HM[1])
        if M==60:M=0
        if H==12:H=0
        angle=Angle(H,M)
        MinimumAngle=min(angle,360-angle)
        print(math.floor(MinimumAngle))
