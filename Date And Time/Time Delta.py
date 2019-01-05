from datetime import datetime
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        t=abs(int((t1-t2).total_seconds()))
        print(t)
