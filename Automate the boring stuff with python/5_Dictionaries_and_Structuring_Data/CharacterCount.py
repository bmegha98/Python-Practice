if __name__ == '__main__':
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    d = dict()
    for ch in message:
        d.setdefault(ch,0)
        d[ch]+=1
    print(d)
