def commalist(lst):
    s = ''
    if lst == []:return s
    if len(lst) == 1 : return lst[0]
    
    tmp = lst[:len(lst)-1]
    s = ', '.join(tmp)
    s = s + ', and ' + lst[-1]
    return s

if __name__ == '__main__':

    l = list(input('Enter elements of list : ').split())
    print(commalist(l))
