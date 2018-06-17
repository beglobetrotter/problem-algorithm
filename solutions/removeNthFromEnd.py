class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
            if not fast:
                break
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

example = solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(head)
output = example.removeNthFromEnd(head, 2)
while output:
    print(output.val)
    output = output.next