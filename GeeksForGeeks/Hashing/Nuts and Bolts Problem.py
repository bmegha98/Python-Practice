'''
Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and
bolts efficiently.
Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only 
be compared with nut to see which one is bigger/smaller.
For each test case, output the matched array of nuts and bolts in separate lines, where each element in the array is separated by a space. 
Print the elements in the following order ! # $ % & * @ ^ ~ 
'''
if __name__ == '__main__':
    T = int(input())
    v = ['!','#', '$', '%', '&' ,'*', '@', '^', '~'] 
    for _ in range(T):
        N = int(input())
        nuts = list(input().split())
        bolts = list(input().split())
        u = []
        for ch in v:
            if ch in nuts and ch in bolts:
                u.append(ch)
        print(*u)
        print(*u)
        
