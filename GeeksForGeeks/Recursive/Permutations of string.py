'''
Given a string S. The task is to print all permutations of a given string.
'''
from itertools import permutations
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        for i in sorted(permutations(S)):
            print(''.join(i),end=' ')
        print()
        
