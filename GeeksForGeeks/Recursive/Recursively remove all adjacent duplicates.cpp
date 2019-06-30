/*
Given a string s, recursively remove adjacent duplicate characters from the string s. 
The output string should not have any adjacent duplicates.
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string str;
        cin>>str;
        int l =str.length();
        stack <char> s;
        int i,flg=0;
        while(1)
        {
            s.push(str[0]);
            l = str.length();
            int dup = 0;
            for(i=1;i<l;i++)
            {
                
                if(!s.empty() && s.top()==str[i])
                {
                    dup = 1;
                    while(i<l && s.top()==str[i])
                    {
                        i++;
                    }
                    s.pop();
                    if(i!=l)
                    {
                        s.push(str[i]);
                    }
                }
                else
                {
                    s.push(str[i]);
                }
                
            }
            if(dup==0)
            {
                break;
            }
            
            str.clear();
            while(!s.empty())
            {
                str+=s.top();
                s.pop();
            }
            reverse(str.begin(),str.end());

        }
        
        cout<<str<<"\n";
    }
}

# In Python

if __name__ =='__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        st = []
        
        while True:
            st.append(s[0])
            dup = 0
            l = len(s)
            i = 1
            while i <l:
                if st!=[] and st[-1]== s[i]:
                    dup = 1
                    while i<l and st[-1] == s[i]:i+=1
                    st.pop()
                    if i!=l:st.append(s[i])
                else:
                    st.append(s[i])
                i+=1
            
            if dup == 0 : break
            tmp = ''
            while st!=[]:
                tmp+= st[-1]
                st.pop()
            s = tmp[::-1]
            if s=='':break
        print(s)
        


