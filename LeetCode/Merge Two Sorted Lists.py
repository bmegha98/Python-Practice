'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first
two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        counter1 , counter2 = l1,l2
        head = l3
        while counter1 and counter2:
            if counter1.val < counter2.val:
                l3.next = counter1
                counter1 = counter1.next
            else:
                l3.next = counter2
                counter2 = counter2.next
            l3 = l3.next
        if counter1:
            l3.next = counter1
        else:
            l3.next = counter2
        
        return head.next
                
