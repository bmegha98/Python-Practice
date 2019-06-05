'''
Given strings s1 and s2, you need to find if s2 is a rotated version of the string s1. The strings are lowercase.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s1 = input()
        s2 = input()
       
        if len(s1)==len(s2):
            tmp = s1+s1             # It gives all possible rotations
            if s2 in tmp : print(1) # of a string.
            else : print(0)
        else:
            print(0)
            
