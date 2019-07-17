# Given a string, remove spaces from it

if __name__ == '__main__':
    T = int(input())
    while T>0:
        print(''.join(list(input().split())))
        T-=1
