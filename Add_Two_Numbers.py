# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself. Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    p, q, curr = l1, l2, dummy
    carry = 0
    
    # Time Complexity: O(max(m, n))
    # Space Complexity: O(max(m, n))
    
    while p != None or q != None:
        x = p.val if p != None else 0
        y = q.val if q != None else 0
        sum = carry + x + y
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        if p != None: p = p.next
        if q != None: q = q.next
    
    if carry > 0:
        curr.next = ListNode(carry)
    
    return dummy.next
