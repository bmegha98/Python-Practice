'''
Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.
'2':'abc'
'3':'def'
'4':'ghi'
'5':'jkl'
'6':'mno'
'7':'pqrs'
'8':'tuv'
'9':'wxyz'
'''

d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
def Permutations(arr , s):
    if not arr :
        print(s,end= ' ')
        return
    for ch in d[arr[0]]:
        Permutations(arr[1:],s+ch)
        
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        D = list(input().split())
        s = ''
        Permutations(D,s)
        print()
