# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
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

        if len(lists) == 0:
            return []
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        else:
            return mergeTwoLists(self.mergeKLists(lists[0:len(lists) // 2]), self.mergeKLists(lists[len(lists) // 2:len(lists)]))


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]

example = solution()
result = example.mergeKLists(lists)
temp = []
while result:
    temp.append(str(result.val))
    result = result.next

print("->".join(temp))