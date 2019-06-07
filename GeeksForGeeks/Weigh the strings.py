'''
The weight W of a string is defined by the formula, W = sum of ASCII values of characters in the string. Now, you are given two strings 
S1 and S2, and the task is to find the heavier string.
Print the string with heavier weight. Print "equal"(without quotes) if weight of both strings are equal.
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s1 ,s2 = input() , input()
        sum1 , sum2 = 0 , 0
        for ch in s1:
            sum1+=ord(ch)
        for ch in s2:
            sum2+=ord(ch)
        if sum1<sum2:print(s2)
        elif sum1>sum2:print(s1)
        else:print('equal')
