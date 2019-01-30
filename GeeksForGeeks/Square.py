'''
Given coordinates of four points in a plane, find if the four points form a square or not.
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def Distance(p1,p2):
    d1=((p2.x)-(p1.x))**2
    d2=((p2.y)-(p1.y))**2
    return d1+d2
        
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        points=list(map(int,input().split()))
        a=Point(points[0],points[1])
        b=Point(points[2],points[3])
        c=Point(points[4],points[5])
        d=Point(points[6],points[7])
        l1,l2,l3,l4=Distance(a,b),Distance(b,c),Distance(c,d),Distance(d,a)
        if l1==l3 and l2==l4 and l1!=0:print('1')
        else:print('0')
