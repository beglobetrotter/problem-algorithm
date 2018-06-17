class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, other):
        return self.val < other.val

class solution:
    def mergeTwoLists(self, l1, l2):
        from heapq import heappush, heappop, heapreplace, heapify
        result = mergeList = ListNode(0)
        lists = [l1, l2]
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, curr = h[0]
            if curr.next is None:
                heappop(h)
            else:
                heapreplace(h, (curr.next.val, curr.next))
            mergeList.next = curr
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
