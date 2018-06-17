class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, other):
        return self.val < other.val

class solution:
    def mergeKLists(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        # h = []
        # for n in lists:
        #     heappush(h, (n.val, n))
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, curr = h[0]
            if curr.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (curr.next.val, curr.next))
            node.next = curr
            node = node.next

        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l3, l1, l2]

example = solution()
result = example.mergeKLists(lists)
temp = []
while result:
    temp.append(str(result.val))
    result = result.next

print("->".join(temp))