'''
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the 
string x in the string s. The function returns and integer denoting the first occurrence of the string x in s.
'''
'''
	Your task is to return the index of the pattern
	present in the given string.
	
	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.
	
'''
def strstr(s,p):
    return s.find(p)
