import re

def strip(string , sep = None):

    if sep == None:
        sep = '\s'

    return re.sub(r'^[{0}]+|[{0}]+$'.format(sep),'',string)  #first {0} is replaced by {sep}
    

    
   

if __name__ == '__main__':

    string = input('Enter string :  ')
    sep = input('Enter character to be stripped from both sides -->  ')
    if sep == '':
        print(strip(string))
    else:
        print(strip(string,sep))
