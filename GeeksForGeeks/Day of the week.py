'''
Write a program that calculates the day of the week for any particular date in the past or future.
'''
import calendar
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        DMY=list(map(int,input().split()))
        D,M,Y=DMY[0],DMY[1],DMY[2]
        day=calendar.weekday(Y,M,D)
        print(calendar.day_name[day])
