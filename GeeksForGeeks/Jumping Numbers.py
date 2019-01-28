'''
Given a positive number X. Find all Jumping Numbers smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. 
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
'''
'''
//TLB Error
def Jumping(n):
    l=[]
    if n>9:l=[i for i in range(0,10)]
    for i in range(10,n+1):
        ch=str(i)
        flag=0
        for j in range(len(ch)-1):
            if int(ch[j])!=int(ch[j+1])+1 and int(ch[j])!=int(ch[j+1])-1:
                flag=1
                break
        if flag==0:l.append(ch)
    return l
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        l=Jumping(N)
        print(' '.join(str(ch) for ch in l))
'''
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        if n<=10:
            numbers = [i for i in range(n)]
            print(*numbers)
        else:
            numbers = [i for i in range(10)]
            for a in numbers:
                if a == 0:
                    continue
                prev_n = a*10 + a%10-1
                next_n = a*10 + a%10+1
                if prev_n >= n or next_n>=n:
                    print(*numbers)
                    break
                elif a%10 == 0:
                    numbers.append(next_n)
                elif a%10 == 9:
                    numbers.append(prev_n)
                else:
                    numbers.append(prev_n)
                    numbers.append(next_n)
