import re

if __name__ == '__main__':

    phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneNum.search('My number is 415-555-4242.')
    print(mo.group())
    print(mo.group())
    print(mo.group(1))
    print(mo.group(2))

    areaCode , mainNumber = mo.groups()
    print('area code -->  ',areaCode)
    print('Phone Number -->  ',mainNumber)

    #to match the area code set in parentheses.
    #In this case, you need to escape the ( and ) characters with a backslash.

    Phone = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    matchobject = Phone.search('My number is (415) 555-4242.')
    print('area code -->  ',matchobject.group(1))
    print('Phone Number -->  ',matchobject.group(2))

    #Matching Multiple groups with the Pipe

    heroRegex = re.compile(r'Batman|Tina Fey')
    mo = heroRegex.search('Batman and Tina Fey.')
    print(mo.group())

    mo = heroRegex.search('Tina Fey and Batman.')
    print(mo.group())

    multiplehero = re.compile(r'Bat(man|mobile|copter\bat)')
    mo = multiplehero.search('Batmobile lost a wheel')
    print(mo.group())
    print(mo.group(1))

    #Optional Matching with a question mark (zero or only one time)

    batRegex = re.compile(r'Bat(wo)?man')
    mo = batRegex.search('The Adventures of Batman')
    print(mo.group())

    mo = batRegex.search('The Adventures of Batwoman')
    print(mo.group())

    #Matching zero or more with the star(zero or multiple times)

    batRegex = re.compile(r'Bat(wo)*man')
    mo = batRegex.search('The Adventures of Batman')
    print(mo.group())

    mo = batRegex.search('The Adventures of Batwowowowoman')
    print(mo.group())

    #Matching one or more with the plus (atleast once)

    batRegex = re.compile(r'Bat(wo)+man')
    mo = batRegex.search('The Adventures of Batwoman')
    print(mo.group())

    mo = batRegex.search('The Adventures of Batwowowowoman')
    print(mo.group())

    #Matching specific repititions with curly brackets

    haRegex = re.compile(r'(Ha){3,5}')          #greedy version --> gives matched text : 'HaHaHaHaHa' i.e. longest string possible
    mo = haRegex.search('HaHaHaHaHa')
    print(mo.group())

    haRegex = re.compile(r'(Ha){3,5}?')          #non-greedy version --> gives matched text : 'HaHaHa' i.e. shortest string possible
    mo = haRegex.search('HaHaHaHaHa')
    print(mo.group())
    
    #The findall() Method

    mo = phoneNum.search('Cell: 415-555-9999 Work: 212-555-0000')
    print('By using search()-- ',mo.group())

    mo = phoneNum.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print('By using findall()-- ',mo)

    #Character Class
    '''
    The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by
    one or more letter/digit/underscore characters (\w+).
    '''

    xmasRegex = re.compile(r'\d+\s\w+')
    mo = xmasRegex.findall('12 drummers, 11 pipers$v, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
    print(mo)

    #Own Character class

    vowRegex = re.compile('[aeiouAEIOU]')
    mo = vowRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(mo)

    consRegex = re.compile('[^aeiouAEIOU]')
    mo = consRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(mo)

    #Caret and Dollar characters

    begins = re.compile(r'^Hello')
    if begins.search('Hello World!')==None:
        print('False')
    else: print('True')

    if begins.search('hello World!')==None:
        print('False')
    else: print('True')

    ends = re.compile(r'\d$')
    if ends.search('xyz 123') == None:
        print('False')
    else:print('True')

    if ends.search('xyz 12a') == None:
        print('False')
    else:print('True')

    both = re.compile('^\d+$')
    if both.search('7838837178') == None:
        print('False')
    else:
        print('True')
        print((both.search('7838837178')).group())

    if both.search('9811abc419') == None:
        print('False')
    else:
        print((both.search('9811abc419')).group())
        print('True')

    #The WildCard Character

    atRegex = re.compile(r'.at')
    print(atRegex.findall('The cat in the hat sat on the flat mat.'))

    nongreedyRegex = re.compile(r'<.*?>')
    mo = nongreedyRegex.search('<To serve man> for dinner.>')
    print(mo.group())

    greedyRegex = re.compile(r'<.*>')
    mo = greedyRegex.search('<To serve man> for dinner.>')
    print(mo.group())

    #Matching Newlines with Dot Character

    noNewlineRegex = re.compile('.*')
    print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
    newlineRegex = re.compile('.*', re.DOTALL)
    print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

    #Case Insensitive Matching

    robocop = re.compile(r'robocop', re.I)
    print(robocop.search('RoboCop is part man, part machine, all cop.').group())
    print(robocop.search('ROBOCOP protects the innocent.').group())
    print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

    #Substituting Strings with sub() method

    regex = re.compile(r'Agent \w+')
    modified = regex.sub('*****','Agent Alice gave the secret documents to Agent Bob.')
    print(modified)

    regex = re.compile(r'Agent (\w)(\w)*')
    modified = regex.sub(r'\1****','Agent Alice gave the secret documents to Agent Bob.')
    print(modified)

    #Combining all modes

    regex = re.compile('foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)
    
                
                
    
    
    

    

    
    
    
