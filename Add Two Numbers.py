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
        carry = 0
        ans = ListNode(0)
        temp = ans
        while l1 and l2:
            i = l1.val
            j = l2.val
            ans.val = (i + j + carry)%10 
            # print(ans.val)
            if i+j+carry>=10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 == None:
                if carry == 1:
                    ans.next = ListNode(1)
                break
            ans.next = ListNode(0)
            ans = ans.next
        
        # the last must get value
        last = l1 if l1 else l2
        while last:
            ans.val = (last.val + carry)%10
            carry = 1 if last.val + carry >=10 else 0
            if last.next == None:
                break
            ans.next = ListNode(0)
            ans = ans.next
            last = last.next
        if carry == 1:
            ans.next = ListNode(1)
            
        return temp

# however , the popular answer is ...
#  tusizi 
# Reputation:  1,365
# class Solution:
# # @return a ListNode
# def addTwoNumbers(self, l1, l2):
#     carry = 0
#     root = n = ListNode(0)
#     while l1 or l2 or carry:
#         v1 = v2 = 0
#         if l1:
#             v1 = l1.val
#             l1 = l1.next
#         if l2:
#             v2 = l2.val
#             l2 = l2.next
#         carry, val = divmod(v1+v2+carry, 10)
#         n.next = ListNode(val)
#         n = n.next
#     return root.next
