'''
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        l = list(s.split('.'))
        l.reverse()
        print('.'.join(l))
