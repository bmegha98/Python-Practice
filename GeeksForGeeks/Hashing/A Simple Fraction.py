'''
Given a fraction. Convert it into a decimal. So simple :P
eg.
10/2 = 5
3/5 = 0.6

(The Question Begins Now)  :D
If the decimals are repeating recursively, then enclose them inside  ().

eg.
8/3 = 2.(6)

as 8/3 = 2.66666666.......  infinitly.   
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num ,den = int(input()),int(input())
        print(num//den,end='')
        k = num%den
        if k == 0:
            print(end='\n')
            continue
        
        frac = [k]
        start = -1
        
        while True:
            k = (k*10)%den
            if k == 0:
                break
            if k in frac:
                start = frac.index(k)
                break
            frac.append(k)
            
        print('.',end='')
        for i in range(len(frac)):
            if i == start: print('(', end='')
            print(int((frac[i]*10)/den), end='')
        
        if start > -1: print(')')
        else: print()
