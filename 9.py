def solve(s):
    for x in s.split():
        s=s.replace(x,x.capitalize())
    return s
   

if __name__ == '__main__':
    S=input()
    res=solve(S)
    print(res)
