class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def mergeTwoLists(self, l1, l2):
        result = mergeList = ListNode(0)
        while l1 or l2:
            if not l1:
                mergeList.next = l2
                l2 = l2.next
            elif not l2:
                mergeList.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    mergeList.next = l1
                    l1 = l1.next
                else:
                    mergeList.next = l2
                    l2 = l2.next
            mergeList = mergeList.next
        return result.next

example = solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = example.mergeTwoLists(l1, l2)
temp = []
while result:
    temp.append(str(result.val))
    result = result.next

print("->".join(temp))
