# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    
    def __init__(self):
        self.head = None
        
    def generateCarry(self, value):
        
        if value > 0:
            number_of_digits = math.floor(math.log10(value) + 1)
        
        else:
            number_of_digits = 1
        
        if number_of_digits > 1:
            to_be_stored_digit = value % 10
            carry = value//10
            
        else:
            to_be_stored_digit = value
            carry = 0
            
        return carry, to_be_stored_digit

        
    def insertValue(self, value):
        
        new_node = ListNode(value)
         
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        
        while last.next:
            last = last.next
        
        last.next = new_node
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        list_Res = Solution()
        
        while l1 or l2:
        
            if not l1:
                answer = l2.val + carry
                carry, result_value = self.generateCarry(answer)
                l2 = l2.next
                list_Res.insertValue(result_value)

            elif not l2:
                answer = l1.val + carry
                carry, result_value = self.generateCarry(answer)
                l1 = l1.next
                list_Res.insertValue(result_value)

            else:
                answer = l1.val + l2.val + carry
                carry, result_value = self.generateCarry(answer)
                l1 = l1.next
                l2 = l2.next
                list_Res.insertValue(result_value)
        
        while carry != 0:
            carry, result_value = self.generateCarry(carry)
            list_Res.insertValue(result_value)
        
        return list_Res.head