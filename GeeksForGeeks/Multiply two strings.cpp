'''
Given two numbers as stings s1 and s2 your task is to multiply them. You are required to complete the function multiplyStrings which takes 
two strings s1 and s2 as its only argument and returns their product as strings.
'''
#include <string>
#include <vector>
string multiply(string s1 ,string s2)
{
    int n1 = s1.length();
    int n2 = s2.length();
    if(n1==0 || n2==0)
    return "0";
    vector<int> result(n1+n2,0);
    int i_n1 =0 , i_n2 =0;
    
    for(int i= n1-1;i>=0;i-- )
    {
        int carry = 0;
        int num1 = s1[i]-'0';
        i_n2 = 0;
        
        for(int j= n2-1 ; j>=0 ; j--)
        {
            int num2 = s2[j]-'0';
            
            int sum = num1*num2 + carry + result[i_n1+i_n2];
            carry = sum/10;
            result[i_n1+i_n2] = sum%10;
            
            i_n2++;
        }
        
        if(carry>0)
        {
            result[i_n1 + i_n2] += carry; 
        }
        i_n1++;
    }
    
    int i = result.size()-1;
    while(i>=0 && result[i]==0)
    i--;
    
    if(i==-1)
    return "0";
    
    string s = "";
    while(i>=0)
    {
        s+=to_string(result[i]);
        i--;
    }
    
    return s;
}
string multiplyStrings(string s1, string s2) 
{
    if((s1[0]=='-' || s2[0] == '-' ) && (s1[0]!='-' || s2[0] != '-') && (multiply(s1,s2)!="0"))
    cout<<'-';
    if( s1[0] == '-' && s2[0]!='-')
    s1 = s1.substr(1);
    else if(s2[0]=='-' && s1[0]!= '-')
    s2 = s2.substr(1);
    else if(s1[0] == '-' && s2[0] == '-')
    {
        s1 = s1.substr(1);
        s2 = s2.substr(1);
        
    }
    
    return multiply(s1,s2);
   
}
