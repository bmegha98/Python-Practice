'''
Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates
of two points: the left top corner and the right bottom corner of the rectangle.
Two rectangles sharing a side are considered overlapping.
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
def Overlap(l1,r1,l2,r2):
    if l1.x>r2.x or l2.x>r1.x:
        return False
    if l1.y< r2.y or l2.y<r1.y:
        return False
    return True

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        rec1=list(map(int,input().split()))
        l1=Point(rec1[0],rec1[1])
        r1=Point(rec1[2],rec1[3])
        rec2=list(map(int,input().split()))
        l2=Point(rec2[0],rec2[1])
        r2=Point(rec2[2],rec2[3])
        if Overlap(l1,r1,l2,r2):
            print('1')
        else:
            print('0')
