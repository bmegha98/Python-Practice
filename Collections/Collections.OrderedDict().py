from collections import OrderedDict
if __name__=='__main__':
    N=int(input())
    superMarket=OrderedDict()
    for i in range(N):
        item_price=input().split()
        l=len(item_price)
        item=' '.join(item_price[0:l-1])
        price=int(item_price[-1])
        if item not in superMarket.keys():
            superMarket[item]=0
        superMarket[item]+=price
    for item,price in superMarket.items():
        print(item,price)
