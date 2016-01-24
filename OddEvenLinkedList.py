# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = 1
        if head!=None :
            odd_list = head
        else:
            return head
        if head.next!=None:
            even_list = head.next
        else:
            return head
        temp_head = odd_list
        temp_head_even = even_list
        while odd_list.next!=None and even_list.next!=None:
            #if odd_list.next !=None:
                odd_list.next = odd_list.next.next
                odd_list = odd_list.next
            #if even_list.next !=None:    
                even_list.next = even_list.next.next
                even_list = even_list.next
        if even_list!= None and even_list.next !=None:
            odd_list.next = odd_list.next.next
            odd_list = odd.next
        odd_list.next = temp_head_even
        head = temp_head
        return head
        
                
        
