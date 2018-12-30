def print_rangoli(size):
    s='abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,0,-1):
        l=[]
        m='-'.join(s[i:size])
        l.append(m[::-1]+m[1::])
        print(''.join(l).center((4*n-3),'-'))
    for i in range(size):
        l=[]
        m='-'.join(s[i:size])
        l.append(m[::-1]+m[1::])
        print(''.join(l).center((4*n-3),'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
