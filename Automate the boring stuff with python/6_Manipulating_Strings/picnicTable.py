def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(17,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth ,'.') + str(v).rjust(rightWidth))

if __name__ == '__main__':
    picnicItems = {'sandwiches':4 , 'apples':12 , 'cups':4 , 'cookies':8000}
    printPicnic(picnicItems,12,5)
    printPicnic(picnicItems,16,8)
