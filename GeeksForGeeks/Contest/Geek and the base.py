'''
The task is to convert decimal numbers(base 10) to the ternary numbers(base 3).
'''
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))
    
if __name__ == '__main__':
    
    T = int(input())
    for _ in range(T):
        
        N =  int(input())
        
        print(ternary(N))
            
