import copy 
if __name__ == '__main__':

    spam = ['A','B','C','D']    # list reference is assigned to variable spam
    cheese = spam               # refernce is copied not the actual list i.e. they refer to same list
    cheese[1] = 42
    print('spam : ' ,spam)
    print('cheese : ',cheese)

    list1 = ['Hi' ,'Hello' ,'Hey' ,'Hola']
    list2 = copy.copy(list1)    # copy function makes a duplicate copy of list1
    list2[1] = 'HaHa'
    print('list1 : ',list1)
    print('list2 : ',list2)

    # deepcopy() is used to duplicate inner lists as well

    il = [[1,2,3],'a','b','c']
    il2 = copy.deepcopy(il)
    il2[0][2] = 6
    print(il)
    print(il2)
