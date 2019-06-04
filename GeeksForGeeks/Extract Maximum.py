'''
You have been given an alphanumeric string S, extract maximum numeric value from that string. Alphabets will only be in lower case.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        numbers = []
        temp =[]
        for ch in S:
            if ch.isdigit():
                temp.append(ch)
               
            elif temp!=[]:
                num = ''.join(temp)
                numbers.append(int(num))
                temp =[]
        if temp!=[]:
            num = ''.join(temp)
            numbers.append(int(num))
            
        print(max(numbers))
