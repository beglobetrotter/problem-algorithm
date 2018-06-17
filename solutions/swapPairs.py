class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            c = b.next
            pre.next = b
            b.next = a
            a.next = c
            pre = a
        return dummy.next

example = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
output = example.swapPairs(head)
temp = []
while output:
    temp.append(str(output.val))
    output = output.next

print("->".join(temp))


