# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Solution 1
"""
class solution(object):
    def addTwoNumbers(self, l1, l2):
        result = end = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry = v1 + v2 + carry
            end.next = ListNode(int(carry % 10))
            end = end.next
            """end.next = end = ListNode(int(carry % 10))"""
            carry = int(carry / 10)
        return result.next

l1 = ListNode(5)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(8)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

example = solution()
result = example.addTwoNumbers(l1, l2)

while result:
    print(result.val, end = "->")
    result = result.next