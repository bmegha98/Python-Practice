'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their 
nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 : return None
        if not l1 : return l2
        if not l2 : return l1
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        num = int(num1[::-1]) + int(num2[::-1])
        num = str(num)[::-1]
        
        HEAD = ListNode(int(num[0]))
        node = HEAD
        
        for i in range(1,len(num)):
            node.next = ListNode(int(num[i]))
            node = node.next
        
        return HEAD
            
            
