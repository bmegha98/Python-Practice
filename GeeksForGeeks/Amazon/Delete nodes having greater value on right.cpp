/*
Given a singly linked list, remove all the nodes which have a greater value on right side.
*/

#include<bits/stdc++.h>
using namespace std;
struct Node
{
int data;
Node* next;
};
Node *newNode(int data)
{
    Node *new_node = new Node;
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}
void print(Node *root)
{
Node *temp = root;
while(temp!=NULL)
{
cout<<temp->data<<" ";
temp=temp->next;
}
}
Node *compute(Node *head);
int main()
{
    int T;
	cin>>T;
	while(T--)
	{
		int K;
		cin>>K;
		struct Node *head = NULL;
        struct Node *temp = head;
		for(int i=0;i<K;i++){
		int data;
		cin>>data;
			if(head==NULL)
			head=temp=newNode(data);
			else
			{
				temp->next = newNode(data);
				temp=temp->next;
			}
		}
        Node *result = compute(head);
        print(result);
        cout<<endl;
    }
}

Node *compute(Node *head)
{
  Node *curr = head;
  Node *prev = NULL , *q = NULL;
  while(curr != NULL)
  {
      q = curr->next;
      curr->next = prev;
      prev = curr;
      curr = q;
  }
  
  Node *R = prev;
  Node *p = R;
  int max = p->data;
  while(p->next != NULL)
  {
      if(p->next->data < max)
      {
          p->next = (p->next != NULL)? p->next->next : NULL;
      }
      else
      {
          max = p->next->data;
          p = p->next;
      }
  }
  
  Node *Curr = R;
  Node *Prev = NULL , *Q = NULL;
  while(Curr != NULL)
  {
      Q = Curr->next;
      Curr->next = Prev;
      Prev = Curr;
      Curr = Q;
  }
  
  return Prev;
}
