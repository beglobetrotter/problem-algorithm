# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for i in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                    #a = cur.next
                    #cur.next = pre
                    #pre = cur
                    #cur = a
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

example = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
output = example.reverseKGroup(head, 4)
temp = []
while output:
    temp.append(str(output.val))
    output = output.next

print("->".join(temp))