# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        def kGroup(head, firstElement, k, result):
            i = (firstElement // 2) - 1
            dummy = pre = ListNode(0)
            pre.next = head
            while pre.next:
                firstNode = endNode = beforeEndNode = validTest = pre.next
                step, move = 0, 0
                while validTest and validTest.next:
                    validTest = validTest.next
                    if step < i:
                        pre = pre.next
                        firstNode = firstNode.next
                    if step < k - 1 - i - 1:
                        beforeEndNode = beforeEndNode.next
                    if step < k - 1 - i:
                        endNode = endNode.next
                    step += 1
                    if step == k - 1:
                        break
                if step < k - 1:
                    break
                a = firstNode.next
                b = endNode.next
                if k % 2 == 0 and i == (k // 2 - 1):
                    pre.next = endNode
                    endNode.next = firstNode
                    firstNode.next = b
                else:
                    pre.next = endNode
                    endNode.next = a
                    beforeEndNode.next = firstNode
                    firstNode.next = b
                if i == 0:
                    pre = firstNode
                else:
                    while move < i:
                        firstNode = firstNode.next
                        pre = firstNode
                        move += 1
            if i == 0:
                result.next = dummy.next
            else:
                firstElement = firstElement - 2
                kGroup(dummy.next, firstElement, k, result)

        if k <= 1 or not head:
            return head
        else:
            result = ListNode(0)
            result.next = head
            kGroup(head, k, k, result)
            return result.next

example = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
output = example.reverseKGroup(head, 1)
temp = []
while output:
    temp.append(str(output.val))
    output = output.next

print("->".join(temp))