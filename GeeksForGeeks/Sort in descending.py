'''
Given a string S containing only lower case alphabets, the task is to sort it in lexigraphically-descending order.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = list(input())
        s.sort(reverse = True)
        print(''.join(s))
